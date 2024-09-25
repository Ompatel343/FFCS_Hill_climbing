# 6th version

import random
import copy

# Sample courses with their respective slots
COURSES = {
    'ARTIFICIAL INTELLIGENCE': ['E1+TE1', 'E2+TE2'],
    'OPERATING SYSTEMS': ['B1+TB1', 'B2+TB2'],
    'OPERATING SYSTEMS LAB': [
        'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
        'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
        'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60',
        'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
        'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
        'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
    ],
    'AWS SOLUTIONS ARCHITECT': ['F1+TF1', 'F2+TF2'],
    'COMPILER DESIGN': ['C1+TC1', 'C2+TC2'],
    'COMPILER DESIGN LAB': [
        'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
        'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
        'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60',
        'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
        'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
        'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
    ],
    'DATABASE SYSTEMS': ['A1+TA1', 'A2+TA2'],
    'DATABASE SYSTEMS LAB': [
        'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
        'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
        'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60',
        'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
        'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
        'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
    ],
    'COMPUTER NETWORKS': ['D1+TD1', 'D2+TD2'],
    'COMPUTER NETWORKS LAB': [
        'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40',
        'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50',
        'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60',
        'L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10',
        'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20',
        'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30'
    ],
    'ADVANCED COMPETITIVE CODING': ['G1+TG1', 'G2+TG2']
}

# Theory slot timings with multiple entries per slot
THEORY_SLOTS = {
    'A1': [('MON', '08:00', '08:50'), ('WED', '09:00', '09:50')],
    'TA1': [('FRI', '10:00', '10:50')],
    'B1': [('TUE', '08:00', '08:50'), ('THU', '09:00', '09:50')],
    'TB1': [('MON', '11:00', '11:50')],
    'C1': [('WED', '08:00', '08:50'), ('FRI', '09:00', '09:50')],
    'TC1': [('TUE', '11:00', '11:50')],
    'D1': [('THU', '08:00', '08:50'), ('MON', '10:00', '10:50')],
    'TD1': [('FRI', '12:00', '12:50')],
    'E1': [('FRI', '08:00', '08:50'), ('TUE', '10:00', '10:50')],
    'TE1': [('THU', '11:00', '11:50')],
    'F1': [('MON', '09:00', '09:50'), ('WED', '10:00', '10:50')],
    'TF1': [('FRI', '11:00', '11:50')],
    'G1': [('TUE', '09:00', '09:50'), ('THU', '10:00', '10:50')],
    'TG1': [('MON', '12:00', '12:50')],
    # Evening slots
    'A2': [('MON', '14:00', '14:50'), ('THU', '17:00', '17:50')],
    'TA2': [('FRI', '16:00', '16:50')],
    'B2': [('WED', '14:00', '14:50'), ('THU', '18:00', '18:50')],
    'TB2': [('FRI', '17:00', '17:50')],
    'C2': [('THU', '14:00', '14:50'), ('FRI', '18:00', '18:50')],
    'TC2': [('WED', '17:00', '17:50')],
    'D2': [('MON', '16:00', '16:50'), ('FRI', '14:00', '14:50')],
    'TD2': [('THU', '19:00', '19:50')],
    'E2': [('TUE', '16:00', '16:50'), ('FRI', '14:00', '14:50')],
    'TE2': [('THU', '17:00', '17:50')],
    'F2': [('MON', '17:00', '17:50'), ('WED', '16:00', '16:50')],
    'TF2': [('THU', '15:00', '15:50')],
    'G2': [('MON', '15:00', '15:50'), ('FRI', '16:00', '16:50')],
    'TG2': [('WED', '18:00', '18:50')]
}

# Lab slot timings (L1-L60)
LAB_SLOTS = {
    # MONDAY MORNING
    'L1': ('MON', '08:00', '08:50'),
    'L2': ('MON', '08:51', '09:40'),
    'L3': ('MON', '09:51', '10:40'),
    'L4': ('MON', '10:41', '11:30'),
    'L5': ('MON', '11:40', '12:30'),
    'L6': ('MON', '12:31', '13:20'),

    # TUESDAY MORNING
    'L7': ('TUE', '08:00', '08:50'),
    'L8': ('TUE', '08:51', '09:40'),
    'L9': ('TUE', '09:51', '10:40'),
    'L10': ('TUE', '10:41', '11:30'),
    'L11': ('TUE', '11:40', '12:30'),
    'L12': ('TUE', '12:31', '13:20'),

    # WEDNESDAY MORNING
    'L13': ('WED', '08:00', '08:50'),
    'L14': ('WED', '08:51', '09:40'),
    'L15': ('WED', '09:51', '10:40'),
    'L16': ('WED', '10:41', '11:30'),
    'L17': ('WED', '11:40', '12:30'),
    'L18': ('WED', '12:31', '13:20'),

    # THURSDAY MORNING
    'L19': ('THU', '08:00', '08:50'),
    'L20': ('THU', '08:51', '09:40'),
    'L21': ('THU', '09:51', '10:40'),
    'L22': ('THU', '10:41', '11:30'),
    'L23': ('THU', '11:40', '12:30'),
    'L24': ('THU', '12:31', '13:20'),

    # FRIDAY MORNING
    'L25': ('FRI', '08:00', '08:50'),
    'L26': ('FRI', '08:51', '09:40'),
    'L27': ('FRI', '09:51', '10:40'),
    'L28': ('FRI', '10:41', '11:30'),
    'L29': ('FRI', '11:40', '12:30'),
    'L30': ('FRI', '12:31', '13:20'),

    # MONDAY AFTERNOON
    'L31': ('MON', '14:00', '14:50'),
    'L32': ('MON', '14:51', '15:40'),
    'L33': ('MON', '15:51', '16:40'),
    'L34': ('MON', '16:41', '17:30'),
    'L35': ('MON', '17:40', '18:30'),
    'L36': ('MON', '18:31', '19:20'),

    # TUESDAY AFTERNOON
    'L37': ('TUE', '14:00', '14:50'),
    'L38': ('TUE', '14:51', '15:40'),
    'L39': ('TUE', '15:51', '16:40'),
    'L40': ('TUE', '16:41', '17:30'),
    'L41': ('TUE', '17:40', '18:30'),
    'L42': ('TUE', '18:31', '19:20'),

    # WEDNESDAY AFTERNOON
    'L43': ('WED', '14:00', '14:50'),
    'L44': ('WED', '14:51', '15:40'),
    'L45': ('WED', '15:51', '16:40'),
    'L46': ('WED', '16:41', '17:30'),
    'L47': ('WED', '17:40', '18:30'),
    'L48': ('WED', '18:31', '19:20'),

    # THURSDAY AFTERNOON
    'L49': ('THU', '14:00', '14:50'),
    'L50': ('THU', '14:51', '15:40'),
    'L51': ('THU', '15:51', '16:40'),
    'L52': ('THU', '16:41', '17:30'),
    'L53': ('THU', '17:40', '18:30'),
    'L54': ('THU', '18:31', '19:20'),

    # FRIDAY AFTERNOON
    'L55': ('FRI', '14:00', '14:50'),
    'L56': ('FRI', '14:51', '15:40'),
    'L57': ('FRI', '15:51', '16:40'),
    'L58': ('FRI', '16:41', '17:30'),
    'L59': ('FRI', '17:40', '18:30'),
    'L60': ('FRI', '18:31', '19:20'),
}

# Map lab courses to their corresponding theory courses
LAB_TO_THEORY = {
    'OPERATING SYSTEMS LAB': 'OPERATING SYSTEMS',
    'COMPILER DESIGN LAB': 'COMPILER DESIGN',
    'DATABASE SYSTEMS LAB': 'DATABASE SYSTEMS',
    'COMPUTER NETWORKS LAB': 'COMPUTER NETWORKS'
}

def time_to_minutes(time_str):
    h, m = map(int, time_str.split(':'))
    return h * 60 + m

def parse_slot_times(slot_names):
    times = []
    for slot_name in slot_names:
        if slot_name in THEORY_SLOTS:
            for day, start, end in THEORY_SLOTS[slot_name]:
                times.append((day, start, end))
        elif slot_name in LAB_SLOTS:
            day, start, end = LAB_SLOTS[slot_name]
            times.append((day, start, end))
        else:
            print(f"Slot {slot_name} not found in THEORY_SLOTS or LAB_SLOTS.")
    return times

def times_overlap(t1_start, t1_end, t2_start, t2_end):
    return max(t1_start, t2_start) < min(t1_end, t2_end)

def schedule_conflict(schedule, new_times):
    for day, start, end in new_times:
        start_min = time_to_minutes(start)
        end_min = time_to_minutes(end)
        for existing_start, existing_end in schedule.get(day, []):
            existing_start_min = time_to_minutes(existing_start)
            existing_end_min = time_to_minutes(existing_end)
            if times_overlap(start_min, end_min, existing_start_min, existing_end_min):
                return True
    return False

def add_to_schedule(schedule, times):
    for day, start, end in times:
        if day not in schedule:
            schedule[day] = []
        schedule[day].append((start, end))

def remove_from_schedule(schedule, times):
    for day, start, end in times:
        schedule[day].remove((start, end))
        if not schedule[day]:
            del schedule[day]

def compute_gaps(schedule):
    total_gaps = 0
    for day in schedule:
        times = schedule[day]
        intervals = sorted([(time_to_minutes(start), time_to_minutes(end)) for start, end in times])
        for i in range(len(intervals) - 1):
            gap = intervals[i+1][0] - intervals[i][1]
            total_gaps += gap // 10
    return total_gaps

def slot_in_time(slot_option, desired_time):
    slot_names = slot_option.split('+')
    times = parse_slot_times(slot_names)
    for _, start, _ in times:
        start_min = time_to_minutes(start)
        if desired_time == 'morning':
            if start_min >= 900:  # Relaxed constraint
                return False
        elif desired_time == 'evening':
            if start_min < 600:  # Relaxed constraint
                return False
    return True

def generate_initial_timetable(attempts=10):
    for attempt in range(attempts):
        print(f"Attempt {attempt + 1} to generate timetable...")
        for theory_time in ['morning', 'evening']:
            lab_time = 'evening' if theory_time == 'morning' else 'morning'
            timetable = {}
            schedule = {}
            failed = False
            
            # Schedule theory courses
            theory_courses = [course for course in COURSES if course not in LAB_TO_THEORY]
            for course in theory_courses:
                slot_options = [opt for opt in COURSES[course] if slot_in_time(opt, theory_time)]
                if not slot_options:
                    print(f"No slot options found for {course} during {theory_time}")
                    failed = True
                    break
                random.shuffle(slot_options)
                for slot_option in slot_options:
                    times = parse_slot_times(slot_option.split('+'))
                    if not schedule_conflict(schedule, times):
                        timetable[course] = slot_option
                        add_to_schedule(schedule, times)
                        break
                else:
                    print(f"Could not fit {course} in the timetable.")
                    failed = True
                    break
            
            if failed:
                continue  # Try the other theory_time

            # Schedule lab courses
            lab_courses = [course for course in COURSES if course in LAB_TO_THEORY]
            for course in lab_courses:
                # Remove the morning/evening constraint for labs
                slot_options = [opt for opt in COURSES[course]]
                if not slot_options:
                    print(f"No lab slot options found for {course}")
                    failed = True
                    break
                random.shuffle(slot_options)
                for slot_option in slot_options:
                    times = parse_slot_times(slot_option.split('+'))
                    if not schedule_conflict(schedule, times):
                        timetable[course] = slot_option
                        add_to_schedule(schedule, times)
                        break
                else:
                    print(f"Could not fit {course} lab in the timetable.")
                    failed = True
                    break

            if not failed:
                print("Successfully generated a timetable.")
                return timetable, schedule
    
    print("Failed to generate a valid timetable after several attempts.")
    return None, None

def hill_climbing(timetable, schedule):
    current_timetable = copy.deepcopy(timetable)
    current_schedule = copy.deepcopy(schedule)
    current_cost = compute_gaps(current_schedule)
    print(f"Initial number of 10-minute gaps: {current_cost}")
    iteration = 0
    while True:
        neighbors = []
        for course in current_timetable:
            if len(COURSES[course]) <= 1:
                continue
            current_slot_option = current_timetable[course]
            for slot_option in COURSES[course]:
                if slot_option != current_slot_option:
                    if course in LAB_TO_THEORY:
                        theory_course = LAB_TO_THEORY[course]
                        theory_slot_option = current_timetable[theory_course]
                        if slot_in_time(theory_slot_option, 'morning'):
                            desired_lab_time = 'evening'
                        else:
                            desired_lab_time = 'morning'
                        # Allow lab slots in both morning and evening
                    new_timetable = copy.deepcopy(current_timetable)
                    new_schedule = copy.deepcopy(current_schedule)
                    old_times = parse_slot_times(current_slot_option.split('+'))
                    remove_from_schedule(new_schedule, old_times)
                    new_times = parse_slot_times(slot_option.split('+'))
                    if not schedule_conflict(new_schedule, new_times):
                        new_timetable[course] = slot_option
                        add_to_schedule(new_schedule, new_times)
                        cost = compute_gaps(new_schedule)
                        neighbors.append((cost, new_timetable, new_schedule))
        if not neighbors:
            break
        neighbors.sort(key=lambda x: x[0])
        best_neighbor = neighbors[0]
        if best_neighbor[0] < current_cost:
            current_cost = best_neighbor[0]
            current_timetable = best_neighbor[1]
            current_schedule = best_neighbor[2]
            iteration += 1
            print(f"Iteration {iteration}: Number of 10-minute gaps: {current_cost}")
        else:
            break
    return current_timetable, current_schedule

def print_timetable(timetable, schedule, title):
    print(f"\n{title}:")
    for course, slot_option in timetable.items():
        times = parse_slot_times(slot_option.split('+'))
        print(f"{course}:")
        for day, start, end in sorted(times):
            print(f"  {day}: {start} - {end}")
    total_gaps = compute_gaps(schedule)
    print(f"Total number of 10-minute gaps: {total_gaps}")

# Generate initial timetable
timetable, schedule = generate_initial_timetable()
if timetable:
    # Print the initial timetable
    print_timetable(timetable, schedule, "Initial Timetable")
    # Optimize timetable using hill climbing
    optimized_timetable, optimized_schedule = hill_climbing(timetable, schedule)
    # Print the optimized timetable
    print_timetable(optimized_timetable, optimized_schedule, "Optimized Timetable")
else:
    print("Failed to generate an initial timetable.")

