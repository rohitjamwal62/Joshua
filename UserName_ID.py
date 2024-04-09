async def Get_Group_Name_Id(client, group_id, user_id):
    try:
        group_entity = await client.get_entity(group_id)
        async for participant in client.iter_participants(group_entity):
            if participant.id == user_id:
                return {'UserName': participant.username, 'User_Id': participant.id}
    except Exception as e:
        print(f"Error in Get_Group_Name_Id: {e}")
    return {}
