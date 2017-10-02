from ffpicker.data import fetch

schedule = fetch.schedule(2017, 3)
print(schedule)
schedule.save()

fetch.game()
