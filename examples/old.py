if user_to_follow not in user_already_followed.keys():
                account_to_follow.append(user_to_follow)
                print(media)
                print(account_to_follow)
                cl.user_follow(cl.user_id_from_username(account_to_follow[media]))
                print(account_to_follow[media])  
                #sleep_time = randint(0, 5)
               # print(sleep_time)
                #for remaining in range(sleep_time, 0, -1):
                  #  sys.stdout.write("\r")
                  #  sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                  #  sys.stdout.flush()
                  #  time.sleep(1)
                  #  sys.stdout.write("\rComplete!            \n")

        elif user_to_follow in user_already_followed.keys(): 
            newmedia = cl.hashtag_medias_top('model', amount=11)
            account_to_follow.append(user_to_follow)
            print(media)
            print(account_to_follow)
            print('ifworking')
            cl.user_follow(cl.user_id_from_username(account_to_follow[10]))
            print(account_to_follow[media])  
           # sleep_time = randint(0, 5)
           # print(sleep_time)
           # for remaining in range(sleep_time, 0, -1):
              #          sys.stdout.write("\r")
               #         sys.stdout.write("{:2d} seconds remaining.".format(remaining))
               #         sys.stdout.flush()
                #        time.sleep(1)
                 #       sys.stdout.write("\rComplete!            \n")
