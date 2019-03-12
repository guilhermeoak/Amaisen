def whatToSay(hour):
    if hour >= 00 and hour < 12:
        return 'Good morning'
    if hour >= 12 and hour < 18:
        return 'Good afternoon'
    if hour >= 18 and hour <= 23:
        return 'Good evening'