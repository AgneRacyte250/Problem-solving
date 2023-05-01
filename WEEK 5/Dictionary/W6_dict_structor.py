pop_dict = {"The Matrix":["Keanu Reeves", "Carrie", "Hugo"],
            "Jack Ryan":["Jonh", "Wendell", "Abbie"],
            "Harry Potter":["Daniel","Emma","Rupert"],
            "Friends":["Aniston","Courtney", "Lisa"],
            "The Office":["Steve", "Rain", "Jonch"]}
def get_cast(title):
    if title in pop_dict:
        return pop_dict[title]
    else:
        return []
def add_title(title, cast_list):
    pop_dict[title] = cast_list
def count_actors():
    actors = dict()
    for cast_list in pop_dict.values():
        for actor in cast_list:
            if actor in actors:
                actors[actor] +=1
            else:
                actor[actor] = 1
    return actors 
