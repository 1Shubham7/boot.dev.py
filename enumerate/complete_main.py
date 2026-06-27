def get_quest_log(quests):
    log = []
    for number, quest in enumerate(quests, start=1):
        log.append(f"{number}. {quest}")
    return log
