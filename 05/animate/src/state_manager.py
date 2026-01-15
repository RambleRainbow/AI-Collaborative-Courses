import json
import os
import numpy as np
from manim import *

STATE_DIR = "scene_states"

def ensure_state_dir():
    if not os.path.exists(STATE_DIR):
        os.makedirs(STATE_DIR)

def serialize_mobject(mobject):
    """
    Extracts essential state from a Mobject / VGroup using Deep JSON Serialization.
    Separates Fill and Stroke properties to ensure visual fidelity.
    """
    state = {
        "points": mobject.points.tolist(),
        # Visual Style - Orthogonal Properties
        "fill_color": mobject.get_fill_color().to_hex(),
        "fill_opacity": mobject.get_fill_opacity(),
        "stroke_color": mobject.get_stroke_color().to_hex(),
        "stroke_width": mobject.get_stroke_width(),
        "stroke_opacity": mobject.get_stroke_opacity(),
        # Fallback/Composite
        "color": mobject.get_color().to_hex(), 
    }
    
    # Geometry (Center, W, H) - critical for layout preservation
    state.update({
        "center": mobject.get_center().tolist(),
        "width": mobject.width,
        "height": mobject.height,
    })
    
    # Support for DecimalNumber and ValueTrackers
    if hasattr(mobject, "get_value"):
        try:
            state["number"] = mobject.get_value()
        except:
            pass

    return state

def apply_state(mobject, state_data):
    """
    Applies saved state using Deep restoration strategy.
    """
    # 1. Geometry First (Position & Scale)
    if "center" in state_data:
        mobject.move_to(np.array(state_data["center"]))
    
    if "width" in state_data and mobject.width > 0:
        mobject.scale_to_fit_width(state_data["width"])
    
    # 2. Visual Style - Apply detailed properties if available
    # Fill
    if "fill_color" in state_data:
        mobject.set_fill(color=state_data["fill_color"])
    if "fill_opacity" in state_data:
        mobject.set_fill(opacity=state_data["fill_opacity"])
        
    # Stroke
    if "stroke_color" in state_data:
        mobject.set_stroke(color=state_data["stroke_color"])
    if "stroke_width" in state_data:
        mobject.set_stroke(width=state_data["stroke_width"])
    if "stroke_opacity" in state_data:
        mobject.set_stroke(opacity=state_data["stroke_opacity"])
        
    # Fallback to generic color if specific props missing (for backward compatibility)
    if "color" in state_data and "fill_color" not in state_data:
        mobject.set_color(state_data["color"])

    # 3. Values
    if "number" in state_data and hasattr(mobject, "set_value"):
        mobject.set_value(state_data["number"])

def save_scene_state(scene_name, cast_dict):
    """
    Saves the state of provided cast members.
    cast_dict: { "actor_name": mobject_instance }
    """
    ensure_state_dir()
    data = {}
    for name, mob in cast_dict.items():
        data[name] = serialize_mobject(mob)
        
    path = os.path.join(STATE_DIR, f"{scene_name}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"State saved to {path}")

def load_scene_state(scene_name):
    path = os.path.join(STATE_DIR, f"{scene_name}.json")
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
