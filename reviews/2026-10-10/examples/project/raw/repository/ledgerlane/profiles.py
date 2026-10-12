"""Local access decision helper; not wired to an authentication system."""


def can_view_profile(member, profile):
    return member["company_id"] == profile["company_id"]
