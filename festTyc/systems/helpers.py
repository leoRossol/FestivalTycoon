#GENERAL HELPERS ======================================================================
def get_staff(festival, service_type):
    for staff in festival.hired_staff:
        if staff.type == service_type:
            return staff
    return None