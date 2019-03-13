def whatToSay(hour):
    if 00 <= hour < 12:
        return 'Good morning'
    if 12 <= hour < 18:
        return 'Good afternoon'
    if 18 <= hour <= 23:
        return 'Good evening'
