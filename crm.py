leads_db = []

def save_lead(session_id, message):
    print("💾 Saving lead...")

    leads_db.append({
        "session_id": session_id,
        "message": message,
        "status": "new"
    })

    print("📊 Total leads:", len(leads_db))


def get_leads():
    print("📤 Returning leads:", leads_db)
    return leads_db