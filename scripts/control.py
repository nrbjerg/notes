#!/usr/bin/env python3
import os
import json
import argparse
from dataclasses import dataclass
from typing import List, Dict, Any


path = str


@dataclass()
class Course:
    """Data about a specific course."""

    name: str
    notes: List[path]
    exam: List[path]

    def add_note(self, title: str):
        """Add a note to the current course."""
        n = len(self.notes)
        pass

    def add_exam_presentation(self, title: str):
        """Add an exam presentation to the current course."""
        pass

    def to_dict(self) -> Dict[str, Any]:
        """Convert the course to a dictionary that can be saved as json."""
        pass


def load_courses() -> List[Course]:
    """Load a list of courses."""
    path = os.path.join(os.getcwd(), "courses.json")
    with open(path, "r") as file:
        obj = json.load(file)
        for key, item in obj.items():
            pass


def save_courses(courses: List[Course]):
    """Saves the courses as a json file."""
