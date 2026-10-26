## Business Rules for the Midterm

NO_DISCOUNT = 0.0
SMALL_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
SMALL_DISCOUNT_MIN_GUESTS = 25
NONPROFIT_DISCOUNT_MIN_GUESTS = 100
SERVICE_FEE = 75.00
SERVICE_FEE_LIMIT = 500.00
SIGNOFF_LIMIT = 2500.00
SECOND_CHEF_GUEST_LIMIT = 80
SECOND_CHEF_TOTAL_LIMIT = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    if guests >= NONPROFIT_DISCOUNT_MIN_GUESTS:
        if nonprofit:
            return NONPROFIT_DISCOUNT
        return SMALL_DISCOUNT
    if guests >= SMALL_DISCOUNT_MIN_GUESTS:
        return SMALL_DISCOUNT
    return NO_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_LIMIT:
        discounted_cost = discounted_cost + SERVICE_FEE
    return discounted_cost


def needs_signoff(total: float) -> bool:
    return total > SIGNOFF_LIMIT


def needs_second_chef(guests: int, total: float) -> bool:
    return guests > SECOND_CHEF_GUEST_LIMIT or total >= SECOND_CHEF_TOTAL_LIMIT


def total_booked(events: list) -> float:
    """Return the sum of the event totals for every event."""
    running_total = 0.0
    for event in events:
        running_total += calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
    return running_total


def largest_event(events: list) -> str:
    """Return the client with the largest event total."""
    largest_client = ""
    largest_total = 0.0
    for event in events:
        total = calculate_event_total(
            event["guest_price"], event["guests"], event["nonprofit"]
        )
        if total > largest_total:
            largest_total = total
            largest_client = event["client"]
    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Return one report line for an event."""
    signoff_text = "yes" if signoff else "no"
    chef_text = "yes" if second_chef else "no"
    return (
        f"{client}: ${total:.2f} | sign-off: {signoff_text} | second chef: {chef_text}"
    )
