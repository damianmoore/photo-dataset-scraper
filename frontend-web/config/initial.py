initial_data = {
    'global_settings': {
        'version':                      0,
        'photo_dirs':                   [],
        'cache_dir':                    '/tmp/photo-manager',
    },

    'user_settings': {
        'filter_date_start':            None,
        'filter_date_finish':           None,
    },

    'global_state': {
        'photo_import_tasks_running':       0,
        'photo_import_task_queue':          [],
        'photo_thumbnailer_tasks_running':  0,
        'photo_thumbnailer_task_queue':     [],
    },

    'session_state': {
        'datasets':                     [],
    },
}
