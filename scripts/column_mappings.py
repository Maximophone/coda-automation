
# Key Column(s) for Upserting (Using 'full_name' as the unique identifier)
KEY_COLUMNS_CONTACTS = ['full_name']
KEY_COLUMNS = {
    "contacts": ["full_name"],
    "organisations": ["name"]
}
MAPPINGS = {
    "contacts": {
        'full_name': {
            'column_id': 'c-UxN9lCiThn',
            'column_type': 'text'
        },
        'email': {
            'column_id': 'c-yLo9IXn_jk',
            'column_type': 'email'
        },
        'linkedin': {
            'column_id': 'c-1q58cttZBb',
            'column_type': 'link'
        },
        'notes': {
            'column_id': 'c-29ChN-_6EQ',
            'column_type': 'text'
        },
        'organizations': {
            'column_id': 'c-HxOayBmbv2',
            'column_type': 'lookup_array'
        },
        'phone_number': {
            'column_id': 'c-IhUchsD3s-',
            'column_type': 'text'
        },
        'contact_types': {
            'column_id': 'c-lMbAXaNoog',
            'column_type': 'lookup_array'
        },
        'tags': {
            'column_id': 'c-Y_Udtgdu68',
            'column_type': 'select'
        },
        'date_created': {
            'column_id': 'c-T918s5CU8m',
            'column_type': 'date'
        },
        'last_interaction': {
            'column_id': 'c-Plkf2qCyoP',
            'column_type': 'lookup'
        },
        'pause_ai': {
            'column_id': 'c-XAcGzKHzvm',
            'column_type': 'checkbox'
        },
        'alignment': {
            'column_id': 'c-slStGF0nbb',
            'column_type': 'select'
        },
        'relation': {
            'column_id': 'c-1D3fWZHSbt',  # Replace with actual column ID
            'column_type': 'select'
        },
        'contacts_privileges': {
            'column_id': 'c-bj1ZPqplaj',
            'column_type': 'person_array'  # New column for "Contacts Privilégiés"
        },
    },
    "organisations": {
        'name': {
            'column_id': 'c-7yNphbZhmL',
            'column_type': 'text'
        },
        'notes': {
            'column_id': 'c-i-Pi1Eokja',
            'column_type': 'text'
        },
        'tags': {
            'column_id': 'c-KhU3ROPDrd',
            'column_type': 'select_array'
        }
    }
}
