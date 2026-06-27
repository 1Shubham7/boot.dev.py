def get_quest_log(quests):
    log = []
    for i, quest in enumerate(quests, start=1):
        log.append(f"{i}. {quest}")
    return log
