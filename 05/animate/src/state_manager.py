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
    Extracts essential state from a Mobject / VGroup.
    """
    state = {
        "points": mobject.points.tolist(),
        "color": mobject.get_color().to_hex(),
        "stroke_width": mobject.get_stroke_width(),
        "fill_opacity": mobject.get_fill_opacity(),
        "stroke_opacity": mobject.get_stroke_opacity(),
    }
    # If it has sub-mobjects, we might need recursive handling?
    # For now, simplistic approach: assuming we only save specific named entities.
    # If VGroup, we save its center and scale roughly? 
    # Actually, saving points is enough for geometry, but VGroups often have submobjects.
    # If we are saving a VGroup that contains letters, saving its points directly might not be enough if it's high level.
    # A better approach for Manim is to save the transformation matrix or key attributes (center, width, height).
    # But Manim objects are complex.
    # Strategy V1: Save Center, Width, Height, Color. And assume the object is re-created standardly then transformed.
    
    state.update({
        "center": mobject.get_center().tolist(),
        "width": mobject.width,
        "height": mobject.height,
    })
    return state

def apply_state(mobject, state_data):
    """
    Applies saved state to a Mobject.
    Does NOT restore shape (points) directly because that's complex.
    Instead, it matches Position, Scale (via width/height), and Style.
    """
    if "center" in state_data:
        mobject.move_to(np.array(state_data["center"]))
    
    if "width" in state_data and mobject.width > 0:
        mobject.scale_to_fit_width(state_data["width"])
    
    if "color" in state_data:
        mobject.set_color(state_data["color"])
        
    if "fill_opacity" in state_data:
        mobject.set_fill(opacity=state_data["fill_opacity"])
        
    if "stroke_opacity" in state_data:
        mobject.set_stroke(opacity=state_data["stroke_opacity"])

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
