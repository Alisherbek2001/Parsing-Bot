def parse_post(text):
    # Matnni ikkita qismga bo'ling: sarlavha va tasnif
    parts = text.split('\n\n', 1)
    data = {
        'title': parts[0].strip() if parts else '',
        'description': ''
    }
    
    if len(parts) > 1:
        description = parts[1].rsplit('\n\n', 1)[0].replace('\n', ' ')
        if description.startswith('@'):
            pass
        else:
            description = ' '.join(description.split())
        data['description'] = description
    return data