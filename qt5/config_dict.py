FIO_dict = {'first_name': {"type": "TEXT"},
            'second_name': {"type": "TEXT"},
            'sure_name': {"type": "TEXT"},
            'birthday': {"type": 'DATE'},
            'tel': {"type": "TEXT"},
            'post': {"type": 'COMBO', "SQL": "SELECT id FROM Staff"}
            }
Clients_dict = {'name': {"type": "TEXT"},
                'sore_name': {"type": "TEXT"},
                'birthday': {"type": 'DATE'},
                'tel': {"type": "TEXT"},
                'json_file': {"type": "TEXT"}
                }
Services_dict = {'service': {"type": "TEXT"},
                'price': {"type": "TEXT"},
                'time_duration': {"type": 'TEXT'},
                'post': {"type": "COMBO", "SQL": "SELECT id FROM Staff"}
                }
Finish_services_dict = {'client': {"type": "COMBO", "SQL": "SELECT id FROM Clients"},
                        'service': {"type": "COMBO", "SQL": "SELECT id FROM Services"},
                        'name_doctor': {"type": "COMBO", "SQL": "SELECT id FROM FIO"},
                        'time_start': {"type": "DATETIME"},
                        'time_end': {"type": "DATETIME"}
                        }

Staff_dict = {'post': {"type": "TEXT"},
              'cash': {"type": "TEXT"},
              'office': {"type": "TEXT"}
              }
