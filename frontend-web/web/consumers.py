import json

from channels import Group

from config.managers import global_settings, user_settings, global_state, session_state

from .utils import get_datasets, get_labels


def ws_message(message):
    data = {}
    if message:
        data = json.loads(message['text'])

    if data.get('command'):
        # Getting settings and state
        if data['command'] == 'get_global_settings':
            message.reply_channel.send({
                'text': json.dumps({
                    'global_settings': global_settings.get_all()
                })
            })
        elif data['command'] == 'get_user_settings':
            message.reply_channel.send({
                'text': json.dumps({
                    'user_settings': user_settings.get_all()
                })
            })
        elif data['command'] == 'get_global_state':
            print(global_state.get_all())
            message.reply_channel.send({
                'text': json.dumps({
                    'global_state': global_state.get_all()
                })
            })
        elif data['command'] == 'get_session_state':
            message.reply_channel.send({
                'text': json.dumps({
                    'session_state': session_state.get_all()
                })
            })

        # Getting UI data
        elif data['command'] == 'get_datasets':
            session_state.set('datasets', get_datasets(), message.reply_channel.name)
        elif data['command'] == 'get_labels':
            message.reply_channel.send({
                'text': json.dumps({
                    'labels': get_labels(),
                })
            })


def ws_connect(message):
    message.reply_channel.send({'accept': True})
    Group('ui').add(message.reply_channel)


def ws_disconnect(message):
    Group('ui').discard(message.reply_channel)
