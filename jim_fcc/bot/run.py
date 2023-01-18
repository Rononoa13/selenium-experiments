from booking.booking import Booking
from booking.booking_filtration import BookingFiltration
from booking.booking import driver

# Context manager
with Booking(driver) as bot:
    bot.land_first_page()
    bot.change_currency(currency='EUR')
    bot.select_place_to_go('Pokhara')
    bot.select_date(check_in='2023-01-19', check_out='2023-01-22')
    bot.select_adults(10)
    bot.click_search()
    print("Exiting...")

with BookingFiltration(driver) as bot:
    bot.apply_star_rating(star_value=3)


# bot = Booking(driver)
# bot.land_first_page()