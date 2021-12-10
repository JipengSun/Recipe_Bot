entity = {
    'step_number':['1','2','3','4','5','6','7','8','9'],
    '':[]
}

def intend_build():

    intend_group = {}

    intend_group['greet'] = [
        'Hi',
        'Hello'
    ]
    intend_group['get_recipe'] = [
        'Walk me through a recipe from AllRecipes.com.'
    ]

    intend_group['get_all_ingredients'] = [
        'Show me the ingredients list'
    ]

    intend_group['send_url'] = [
    'https://www.allrecipes.com/recipe/24074/alysias-basic-meat-lasagna/'
    ]
    intend_group['specific_how_to'] = [
        'How do I <specific technique>?',
    ]

    intend_group['specific_what_is'] = [
        'What is a <tool being mentioned>?',
    ]

    intend_group['vague_how_to'] = [
        'How do I do that?'
    ]
    intend_group['get_ingredient_amount_of_current_step'] = [
        'How much of <ingredient> do I need?'
    ]
    intend_group['get_temperature_of_current_step'] = [
        'What temperature?'
    ]
    intend_group['get_time_of_current_step'] = [
        'How long do I <specific technique>',
        'When is it done?',
        'How long do I'

    ]
    intend_group['appreciation'] = [
        'Thanks',
        'thx',
        "Thanks again"
    ]

    intend_group['confirm'] = [
        'Yes, please',
        'yes',
        'OK'
    ]

    intend_group['get_ingredient_substitution'] = [
        'What can I substitute for <ingredient>?'
    ]
    intend_group['forward_one_step'] = [
        'Go to the next step',
        'Next',
        'Next step'
    ]
    intend_group['back_one_step'] = [
        'Go back one step',
        'Previous step'
    ]
    intend_group['goto_specific_step'] = [
        'Take me to the n-th step',
        'Take me to the 1st step',
        'Take me to the 2nd step',
        'Take me to the 3rd step',
        'Take me to the 4th step',
        'Take me to the 5th step',
        'Take me to the 6th step',
    ]
    intend_group['repeat_current_step'] = [
        'Repeat please',
        'Repeat current step',
        'Repeat'
    ]
    intend_group['select_option'] = [
        '1',
        '2'
    ]
    return intend_group

