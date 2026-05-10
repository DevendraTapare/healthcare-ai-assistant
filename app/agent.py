def check_available_slots(department, date):
    return [
        "10:00 AM",
        "2:00 PM",
        "4:30 PM"
    ]


def route_question(question):
    if "appointment" in question.lower():
        return {
            "tool": "appointment_scheduler",
            "slots": check_available_slots("general", "monday")
        }

    return None