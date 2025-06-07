# Montly apartment cost in dollars.
# - Rent, utilities, etc.
monthly_rent = 1200

# Number of months I'd pay rent per year
rent_months_per_year = 12

yearly_rent = monthly_rent * rent_months_per_year

# Number of days I go to school yearly.
# 3 quarters * 11 weeks * 5 days
school_days = 3 * 11 * 5

# How much rent I'll pay per school day
rent_per_school_day = yearly_rent / school_days


# https://transportation.uw.edu/park/student-employee/student
daily_parking_cost = 7.85

# https://wsdot.wa.gov/travel/roads-bridges/toll-roads-bridges-tunnels/sr-520-bridge-tolling
daily_bridge_toll = 8

# Total daily drive distance in miles.
commute_distance = 24

# $4.00/gal and 30 MPG
fuel_cost_per_mile = 4 / 30

# How much $/hr I think I should be paid to endure sitting in a car or bus
# (as opposed to walking to school from apartment),
# ignoring real monetary costs from both options.
# The value of time I waste while commuting.
commute_wage_per_hour = 20

# Total hours per day to commute by car
car_commute_time = 0.75

# Total hours per day to commute by bus
bus_commute_time = 1.5

# How much $/schoolday I think I should be paid to endure living
# at family home (as opposed to an apartment),
# ignoring real monetary costs from both options.
# - Distracting homework environment.
# - Social distance from friends.
# - Reduced experience with independence.
home_wage_per_schoolday = 40

# How much it costs per school day to drive to school.
daily_car_cost = (
    daily_parking_cost
    + daily_bridge_toll
    + commute_distance * fuel_cost_per_mile
    + commute_wage_per_hour * car_commute_time
    + home_wage_per_schoolday
)

# U-pass
daily_bus_cost = 0 + commute_wage_per_hour * bus_commute_time + home_wage_per_schoolday

print(f"Value of time I waste by commuting: ${commute_wage_per_hour:,.2f}/hr  ;)")
print()
print("Cost per school day (including time wasted) to...")
print(f"Live in apartment:  ${rent_per_school_day:,.2f}")
print(f"Commute by car:     ${daily_car_cost:,.2f}")
print(f"Commute by bus:     ${daily_bus_cost:,.2f}")
