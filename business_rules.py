## Business Rules for the Midterm

calculate_food_cost(guest_price: float, guests: int) -> float

get_event_discount(guests: int, nonprofit: bool = False) -> float

calculate_event_total(guest_price: float, guests: int, nonprofit: bool = False) -> float

needs_signoff(total: float) -> bool

needs_second_chef(guests: int, total: float) -> bool

total_booked(events: list) -> float

largest_event(events: list) -> str

format_event_line(client: str, total: float, signoff: bool, second_chef: bool) -> str