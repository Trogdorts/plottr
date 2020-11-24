import random
import string
from faker import Faker
import copy



# Utility Functions

def guid(preamble="", length=16):
    """
    # Create a Globally Unique Identifer
    """
    tmp = []
    tmp.append(preamble.upper())
    uid_len = length - len(preamble)
    uid = str(preamble) + ''.join(random.choices(string.digits, k=uid_len))
    return uid

def build_new_uiverse():
    universe_uid = guid("UNIVERSE")
    universe = {'uid': universe_uid, 'type':'universe'}
    return universe  
    
def build_new_series():
    series_uid = guid("SERIES")
    series = {'uid':series_uid, 'type':'series'}
    series['series_number'] = 0
    return series

def get_series_numbers(universe): 
    _series = []
    for i in universe.keys():
        if 'SERIES' in i:
            uid = universe[i]['uid']
            series_number = universe[i]['series_number']
            _series.append(series_number)
    return _series

def add_series_to_universe(series, universe, add_location='end'):
    """
    Add a new Series to a existing Universe
    The default location is to add it at the end. This leaves room open for
    future dev work to add custom add locations.
    """
    tmp_series = get_series_numbers(universe)
    if add_location.lower() == 'end': # Get the last series in the universe
        if not tmp_series:
            series['series_number'] = 1
        elif add_location == "end":
            last_series = tmp_series.pop()
            new_series= last_series + 1
            series['series_number'] = new_series
    universe[series['uid']] = series
    return universe

def build_new_novel(word_count='novel'):
    """
    # Build a new novel
    """
    def set_word_count(word_count):
        fiction_lengths = {
            'short' : int(7500),
            'novelette' : int(17500),
            'novela' : int(50000),
            'novel' : int(100000),
            'epic' : int(200000),
            }
        if word_count in fiction_lengths.keys():
            word_count = fiction_lengths[word_count]
        if word_count == 'random':
            word_count = fiction_lengths[random.choice(list(fiction_lengths.keys()))]
        return word_count

    def set_pov(pov='random'):
        # https://www.well-storied.com/blog/pov-tense
        point_of_views = {
            'first_person' : {'name':'First Person',
                              'pronouns': ['I', 'we']},
            'first_person_reliable' : {'name':'First Person Reliable',
                                       'pronouns': ['I', 'we']},
            'first_person_unreliable' : {'name':'First Person Unreliable',
                                         'pronouns': ['I', 'we']},
            'second_person' : {'name':'Second Person',
                               'pronouns': ['you']},
            'third_person' : {'name':'Third Person',
                              'pronouns': ['he', 'she', 'it', 'they']},
            'third_person_limited' : {'name':'Third Person Limited',
                                      'pronouns': ['he', 'she', 'it', 'they']},
            'third_person_omniscient' : {'name':'Third Person Omnisicent',
                                         'pronouns': ['he', 'she', 'it', 'they']}
        }
        if ( pov not in point_of_views.keys() or pov == 'random'):
            pov = point_of_views[random.choice(list(point_of_views.keys()))]
        else:
            pov = point_of_views[pov]
        return pov


    def set_available_roles():
        
        # TODO needs to be a function that defines the roles
        """
        # set all the role counts to 0 to be filled in as each character is created and added
        """
        roles = {
            'protagonist' : {'description' : "the character responsible for handling the main problem and the one most in need of change, emotionally.",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'antagonist' : {'description' : "the primary bad guy. The character that opposes the protagonist outright on all counts, physically and emotionally.",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'love_interest' : {'description' : "description goes here",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'confidant' : {'description' : "description goes here",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'mentor' : {'description' : "the protagonist’s conscience and the prevailing side to the thematic argument. The mentor voices or represents the lesson that must be learned by the protagonist in order to change for the better and achieve the goal. (Note: Be mindful of creating a mentor who is as perfect and principled as humans can be, for doing so will make the character seem inhuman. Instead, let the mentor be flawed, like all us humans.)",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'temptor' : {'description' : "the right-hand to the antagonist. The tempter doesn’t need to know the antagonist, but they both stand for the same thing: stopping the protagonist from achieving the protagonist’s goal. The tempter tries to manipulate and convince the protagonist to join the “dark side”. However, in the end, the tempter can change his/her mind and realize the benefit of joining the good guys.",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'skeptic' : {'description' : "the lone objector. The skeptic does not believe in the theme nor in the importance of achieving the protagonist’s goal. Without loyalties, the skeptic is on his/her own path. The skeptic may like the protagonist and want the protagonist to succeed but not at the cost of the skeptic’s goals. However, the skeptic may have a change of heart by the end of the story.",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'emotional' : {'description' : "this character acts according to their gut and lets motions fuel decisions. Impulsive. Reactive. Sometimes the emotional character is right and succeeds in ways that a thinking person would never have even tried, but sometimes the character finds trouble by not thinking before jumping.",
                                'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'logical' : {'description' : "the rational thinker who plans things out, shoots for logical solutions and gives reasonable, matter-of-fact answers to questions. However, sometimes the head needs to listen to the heart to work at its best.",
                         'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0},
            'foil'  : {'description' : "a supporting character who has a contrasting personality and set of values to the protaganist. Putting the foil and main character in close proximity helps draw readers’ attention to the latter’s attributes.",
                       'count' : 0},
            'catalyst'  : { 'description' : "the character in a story who causes the protagonist, or main character, to move toward some kind of action or transformation. This character is usually the person that spends the most quality and influential time with the protagonist.",
                            'count' : 0,
                            'characters' : [],
                            'aka' : '',
                            'unused' : 0}
        }
        return roles
        
        
    novel_uid = guid("NOVEL")
    novel = {'uid':novel_uid}
    novel['word_count'] = set_word_count(word_count)
    novel['average_passage_length'] = 1170
    novel['characters'] = {}
    novel['settings'] = {}
    novel['novel_number'] = 0
    novel['pov'] = set_pov('first_person')
    novel['type'] = 'novel'
    novel['roles'] = set_available_roles()
    return novel

def get_novel_numbers(series): 
    novels = []
    for i in series.keys():
        if 'NOVEL' in i:
            uid = series[i]['uid']
            novel_number = series[i]['novel_number']
            novels.append(novel_number)
    return novels

def add_novel_to_series(novel, series, add_location='end'):
    """
    Add a new novel to a existing Series
    The default location is to add it at the end. This leaves room open for
    future dev work to add custom add locations.
    """
    novels = get_novel_numbers(series)
    if add_location.lower() == 'end': # Get the last novel in the series
        if not novels: 
            novel['novel_number'] = 1
        elif add_location == "end":
            last_novel = novels.pop()
            new_novel = last_novel + 1
            novel['novel_number'] = new_novel
    series[novel['uid']] = novel
    return series

def build_passage_pair(number):
    return {'num':number, 'uid':guid("PSGPAIR"), 'description' : "Passage pairs are made up of a scene and a sequel."}

def build_passages(novel):
    # https://www.helpingwritersbecomeauthors.com/scene-structure-2/
    if 'passages' not in novel:
        novel['passages'] = {}  # Create a key:value pair to store all the passages

    def build_scene():
        scene = {
            'type' : 'scene',
            'goal': {'description' : "character wants something on the scene level that will ultimately help him reach his overall plot goal—and he tries to get it"},
            'conflict': {'description' : "character is met with an obstacle to obtaining his goal"},
            'outcome':{'description' : "usually disastrous, in the sense that the character does not achieve the goal or achieves only part of it"},
            'passage_pair' : {},
            'uid': guid("SCENE")}
        return scene
        
    def build_sequel():
        sequel = {
            'type' : 'sequel',
            'reaction': {'description' : "character reacts to the outcome"},
            'delemma': {'description' : "character must figure out  how to overcome the new complications and still move forward toward his main plot goal"},
            'decision':{'description' : "character decides upon a new scene goal to cope with the new complications and move forward toward the main plot goal in a—hopefully—more effective way"},
            'passage_pair' : {},
            'uid': guid("SEQUEL")}
        return sequel

    num_of_passages = int(novel['word_count'] / novel['average_passage_length'])
    if num_of_passages %2:  # Check to see if there is an odd number of passages.
        num_of_passages -=1 # If passages is an odd number, minus 1 from it.
    passage_pair_cnt = 0
    tmp_pair_cnt = 0
    for n in range(1,num_of_passages+1):
        if tmp_pair_cnt == 0:
            passage_pair_cnt += 1
            passage_pair = build_passage_pair(passage_pair_cnt)
        if n %2: # Create a Scene
            scene = build_scene()
            novel['passages'][n] = scene
            novel['passages'][n]['passage_pair'] = passage_pair
            tmp_pair_cnt = 1
        else: # Create a Sequel
            sequel = build_sequel()
            novel['passages'][n] = sequel
            novel['passages'][n]['passage_pair'] = passage_pair
            tmp_pair_cnt = 0
    return novel

def build_new_character(archetype="random", sex='random', species='human'):

    def set_species(species):
        common_species = {
            'human' : {'name' : "human"}
        }
        if ( species not in common_species.keys() or species == 'random'):
            species = common_species[random.choice(list(common_species.keys()))]
        else:
            species = common_species[species]
        return species

    def set_sex(sex):
        if sex == 'random':
            sex = random.choice(['male','female'])
        return sex
    
    def set_name(sex):
        faker = Faker()
        if sex == 'male':
            first_name = faker.first_name_male()
            last_name = faker.last_name_male()
        elif sex =='female':
            first_name = faker.first_name_female()
            last_name = faker.last_name_female()
        return first_name, last_name
    
    def set_archetype(archetype, character):
        # https://www.storyplanner.com/story/plan/character-archetypes
        character_archetypes = {
                    "The Innocent": {
                        "archetype_name": "The Innocent",
                        "Desire": "to reach paradise",
                        "Goal": "to be happy",
                        "Greatest fear": "to be punished for doing something bad or wrong",
                        "Strategy": "to do things right",
                        "Weakness": "their naive innocence can be boring or lack realism",
                        "Talent": "faith and optimism",
                        "aka": "The utopian, the traditionalist, naive, mystic, saint, romantic, dreamer."
                    },
                    "The Orphan/The Regular Guy": {
                         "archetype_name": "The Orphan/The Regular Guy",
                        "Desire": "connecting with others",
                        "Goal": "to belong",
                        "Greatest fear": "to be left out or to stand out from the crowd",
                        "Strategy": "to develop ordinary solid virtues, be down to earth, the common touch",
                        "Weakness": "losing one's own self in an effort to blend in or for the sake of superficial relationships",
                        "Talent": "realism, empathy, lack of pretence",
                        "aka": "The good old boy, everyman, the person next door, the realist, the solid citizen, the good neighbour, the silent majority."
                    },
                    "The Hero": {
                         "archetype_name": "The Hero",
                        "Desire": "to prove one's worth through courageous acts",
                        "Goal": "expert mastery in a way that improves the world",
                        "Greatest fear": "weakness, vulnerability, being a coward",
                        "Strategy": "to be as strong and competent as possible",
                        "Weakness": "arrogance, always needing another battle to fight",
                        "Talent": "competence and courage",
                        "aka": "The warrior, crusader, rescuer, superhero, the soldier, dragon slayer, the winner and the team player."
                    },
                    "The Caregiver": {
                         "archetype_name": "The Caregiver",
                        "Desire": "to protect and care for others",
                        "Goal": "to help others",
                        "Greatest fear": "selfishness and ingratitude",
                        "Strategy": "doing things for others",
                        "Weakness": "martyrdom and being exploited",
                        "Talent": "compassion, generosity",
                        "aka": "The saint, altruist, parent, helper, supporter."
                    },
                    "The Explorer": {
                         "archetype_name": "The Explorer",
                        "Desire": "the freedom to find out who you are through exploring the world",
                        "Goal": "to experience a better, more authentic, more fulfilling life",
                        "Biggest fear": "getting trapped, conformity, and inner emptiness",
                        "Strategy": "journey, seeking out and experiencing new things, escape from boredom",
                        "Weakness": "aimless wandering, becoming a misfit",
                        "Talent": "autonomy, ambition, being true to one's soul",
                        "aka": "The seeker, iconoclast, wanderer, individualist, pilgrim."
                    },
                    "The Rebel": {
                         "archetype_name": "The Rebel",
                        "Desire": "revenge or revolution",
                        "Goal": "to overturn what isn't working",
                        "Greatest fear": "to be powerless or ineffectual",
                        "Strategy": "disrupt, destroy, or shock",
                        "Weakness": "crossing over to the dark side, crime",
                        "Talent": "outrageousness, radical freedom",
                        "aka": "The rebel, revolutionary, wild man, the misfit, or iconoclast."
                    },
                    "The Lover": {
                         "archetype_name": "The Lover",
                        "Desire": "intimacy and experience",
                        "Goal": "being in a relationship with people, work and surroundings they love",
                        "Greatest fear": "being alone, a wallflower, unwanted, unloved",
                        "Strategy": "to become more and more physically and emotionally attractive",
                        "Weakness": "outward-directed desire to please others at risk of losing own identity",
                        "Talent": "passion, gratitude, appreciation, and commitment",
                        "aka": "The partner, friend, intimate, enthusiast, sensualist, spouse, team-builder."
                    },
                    "The Creator": {
                         "archetype_name": "The Creator",
                        "Desire": "to create things of enduring value",
                        "Goal": "to realize a vision",
                        "Greatest fear": "mediocre vision or execution",
                        "Strategy": "to develop artistic control and skill",
                        "Task": "to create culture, express his own vision",
                        "Weakness": "perfectionism, bad solutions",
                        "aka": "The artist, inventor, innovator, musician, writer or dreamer."
                    },
                    "The Jester": {
                         "archetype_name": "The Jester",
                        "Desire": "to live in the moment with full enjoyment",
                        "Goal": "to have a great time and lighten up the world",
                        "Greatest fear": "being bored or boring others",
                        "Strategy": "play, make jokes, be funny",
                        "Weakness": "frivolity, wasting time",
                        "Talent": "joy",
                        "aka": "The fool, trickster, joker, practical joker or comedian."
                    },
                    "The Sage": {
                         "archetype_name": "The Sage",
                        "Desire": "to find the truth.",
                        "Goal": "to use intelligence and analysis to understand the world.",
                        "Biggest fear": "being duped, misled\u00e2\u20ac\u201dor ignorance.",
                        "Strategy": "seeking out information and knowledge; self-reflection and understanding thought processes.",
                        "Weakness": "can study details forever and never act.",
                        "Talent": "wisdom, intelligence.",
                        "aka": "The expert, scholar, detective, advisor, thinker, philosopher, academic, researcher, thinker, planner, professional, mentor, teacher, contemplative."
                    },
                    "The Magician": {
                         "archetype_name": "The Magician",
                        "Desire": "understanding the fundamental laws of the universe",
                        "Goal": "to make dreams come true",
                        "Greatest fear": "unintended negative consequences",
                        "Strategy": "develop a vision and live by it",
                        "Weakness": "becoming manipulative",
                        "Talent": "finding win-win solutions",
                        "aka": "The visionary, catalyst, inventor, charismatic leader, shaman, healer, medicine man."
                    },
                    "The Ruler": {
                         "archetype_name": "The Ruler",
                        "Desire": "control",
                        "Goal": "create a prosperous, successful family or community",
                        "Strategy": "exercise power",
                        "Greatest fear": "chaos, being overthrown",
                        "Weakness": "being authoritarian, unable to delegate",
                        "Talent": "responsibility, leadership",
                        "aka": "The boss, leader, aristocrat, king, queen, politician, role model, manager or administrator."
                    }
                }
        archetypes = []
        for key in character_archetypes.keys():
            archetypes.append(key)
        if str(archetype) not in archetypes:
            archetype = 'random'
        if archetype == 'random':
            choice = random.choice(archetypes)
        for key, value in character_archetypes[choice].items():
            character[key.lower()] = value
             
    character_uid = guid("CHARACTER")
    character = {'uid':character_uid}
    character['sex'] = set_sex(sex)
    character['first_name'] = set_name(character['sex'])[0]
    character['last_name'] = set_name(character['sex'])[1]
    character['middle_name'] = '' #TODO - write custom module for setting common middle names
    character['full_name'] = " ".join([character['first_name'], character['last_name']])
    character['nickname'] = ''
    character['age'] = ''
    character['species'] = set_species(species)
    character['occupation'] = ''
    character['storyline'] = {}
    character['goal'] = {}
    character['motivation'] = {}
    character['conflict'] = {}
    character['epiphany'] = {}
    character['history'] = []
    character['passages'] = []
    character['roles'] = {'primary' : {}, 'secondary' : {}}


    # Some things have to run after the character is created.
    set_archetype(archetype, character)
    
    return character

def add_character_to_novel(character, novel):
    """
    Characters  are added to the novel.
    """
    novel['characters'][character['uid']] = character

def get_novel_characters(novel):
    """
    Returns a dict of characters in a novel
    """
    characters = []
    for c in novel['characters']:
        characters.append({ c : novel['characters'][c]})
    return characters
    
def pretty_print(universe):
    """
    Prints all the tings I want to see while debugging
    """
    for i in universe.keys():
        if 'SERIES' in i:
            print("Series:", i)
            for n in universe[i].keys():
                if 'NOVEL' in n:
                    print("Novel:", n)
                    print("Word Count:", universe[i][n]['word_count'])
                    print("Total Unused Roles:", get_unused_roles_count(universe[i][n]))
                    print("Point of View:", universe[i][n]['pov']['name'])
                    print("Chapters:", len(list(universe[i][n]['passages'].keys())))
                    for c in universe[i][n]['characters'].keys():
                        
                        print_roles = "Primary: " + list(universe[i][n]['characters'][c]['roles']['primary'].keys())[0]
                        try:
                            print_roles = print_roles + ", Secondary: " + list(universe[i][n]['characters'][c]['roles']['secondary'].keys())[0]
                        except:
                            pass
                        print("Character:", universe[i][n]['characters'][c]['full_name'], '\tRoles:', print_roles )

def get_unused_roles_count(novel):
    roles = 0
    for key in novel['roles'].keys():
        print(novel['roles'][key]['unused'])
        count = novel['roles'][key]['unused']

        roles = roles + count
    return roles

def build_novel_cast(novel, cast_list='default'):
    # by default, enable a single instance of each role. 
    # TOD come back later and add in different cast lists to build for different novel lenghts and genres
    
    def get_available_roles(novel):
        available_roles = []
        for key in novel['roles'].keys():
            count = novel['roles'][key]['unused']
            for n in range(count):
                available_roles.append(key)
        return available_roles
    
    def set_default_roles(novel):
        for key in novel['roles'].keys():
            novel['roles'][key]['unused'] = 1        
    
    if cast_list == 'default':
        set_default_roles(novel)

    if cast_list == 'dev':
        set_default_roles(novel)
        choices_list = []
        for key in novel['roles'].keys():
            choices_list.append(key)
        change_list = random.sample(choices_list, random.randint(1, len(choices_list)))
        for item in change_list:
            if item == 'protagonist' or item == 'catalyst' or item == 'foil':
                change_list.remove(item)
        for key in change_list:
            novel['roles'][key]['unused'] = ++random.randint(1,3)   


    available_roles = get_available_roles(novel)
    unique_roles = list(set(available_roles))
    
    # Create a character for each primary role
    for role in unique_roles:
        character = build_new_character()
        character['roles']['primary'] = {str(role):copy.deepcopy(novel['roles'][role])}
        del character['roles']['primary'][role]['unused'] # dont need this field coppied to the character 
        add_character_to_novel(character, novel)
        available_roles.remove(role) # Remove selected role from the novels available roles
        novel['roles'][role]['unused'] = (novel['roles'][role]['unused'] - 1)
    
    # Distribute out the rest of the roles as secondary to the existing characters
    print("there are {} secondary roles available to be distributed.".format(len(available_roles)))
    while len(available_roles) > 0:
        print(available_roles)
        for role in available_roles:
            characters = get_novel_characters(novel) # get a list of all characters
            random_character = random.choice(characters)
            selected_character = list(random_character.keys())[0]
            # TODO this should be a future logging statement print("Adding secondary role {} to character {}.".format(role, selected_character))
            if (novel['characters'][selected_character]['roles']['primary']) != 'protagonist':  # dont give a second role to the protagonist
                if (novel['characters'][selected_character]['roles']['primary']) != 'temptor':  # dont give a second role to the temptor
                    novel['characters'][selected_character]['roles']['secondary'] = {str(role):copy.deepcopy(novel['roles'][role])}
                    del novel['characters'][selected_character]['roles']['secondary'][role]['unused'] # dont need this field coppied to the character 
                    available_roles.remove(role) # Remove selected role from the novels available roles
                    novel['roles'][role]['unused'] = (novel['roles'][role]['unused'] - 1)

            
                
            
            
        

            
                
        #print()

  
    
    
    

    # Add the selected role to the novels role count
         

    
    
    
    
    
# Future Work
# This is where the novel writer will go
# Right now these are manually building everything
if __name__ == '__main__':


    universe = build_new_uiverse()
    series = build_new_series()
    add_series_to_universe(series, universe)
    novel = build_new_novel(word_count='random')
    add_novel_to_series(novel, series)
    build_passages(novel)

    build_novel_cast(novel, cast_list='dev')


    # Testing Pretty Print Function
    pretty_print(universe)

    import json
    with open("pretty_print.json", 'w') as f:
        print(json.dumps(universe, indent=4), file=f)


'''
    # Test saving json file
    with open('test_json.json', 'w') as outfile:
        json.dump(universe, outfile)
'''      
