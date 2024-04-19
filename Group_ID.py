from telethon.sync import TelegramClient

# Get group name and group id
api_id = '25500977'
api_hash = '7cf41fa26b716a01a46d744758bfbde2'
phone_number = '+61483212824'
THE_AUTIST_KITCHEN_Group_Id = -1001606570958
Macro_Newletter_Alpha4_Group_Id = -1001810340094

Group = -1001606570958 #Edit group id here...............


with TelegramClient('session_name', api_id, api_hash) as client:
    client.start(phone_number)

    # Find the group by its username
    group_entity = client.get_entity(Group)

    # Get all participants in the group
    participants = client.get_participants(group_entity)

    # Print usernames of participants
    for participant in participants:
        if participant.username:
            print(participant.username)
            print(participant.first_name,"===",participant.id)