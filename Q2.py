class Patient:
    def __init__(self, patient_name, arrival_time, treatment_time, urgency_level):
        self.patient_name = patient_name
        self.arrival_time = arrival_time
        self.treatment_time = treatment_time
        self.urgency_level = urgency_level

def first_come_first_served(patients):
    return sorted(patients, key=lambda x: x.arrival_time)

def shortest_job_first(patients):
    return sorted(patients, key=lambda x: x.treatment_time)

def priority_scheduling(patients):
    return sorted(patients, key=lambda x: -x.urgency_level)

def round_robin_scheduling(patients, time_quantum=10):
    queue = []
    current_time = 0
    order = []

    while patients or queue:
        available = [p for p in patients if p.arrival_time <= current_time]
        queue.extend(available)
        for p in available:
            patients.remove(p)

        if queue:
            current_patient = queue.pop(0)
            if current_patient.treatment_time > time_quantum:
                current_time += time_quantum
                current_patient.treatment_time -= time_quantum
                queue.append(current_patient)
            else:
                current_time += current_patient.treatment_time
                order.append(current_patient)
        else:
            current_time += 1

    return order

patients = [
    Patient('P1', 0, 30, 3),
    Patient('P2', 10, 20, 5),
    Patient('P3', 15, 40, 2),
    Patient('P4', 20, 15, 4)
]

fcfs_order = [p.patient_name for p in first_come_first_served(patients)]
sjf_order = [p.patient_name for p in shortest_job_first(patients)]
ps_order = [p.patient_name for p in priority_scheduling(patients)]
rr_order = [p.patient_name for p in round_robin_scheduling(patients)]

print("First Come First Served:", fcfs_order)
print("Shortest Job First:", sjf_order)
print("Priority Scheduling:", ps_order)
print("Round Robin Scheduling:", rr_order)

# Determine the best scheduling algorithm and mention the algorithm name
algorithm_orders = {
    "FCFS": fcfs_order,
    "Shortest Job First": sjf_order,
    "Priority Scheduling": ps_order,
    "Round Robin Scheduling": rr_order
}

best_algorithm_name = min(algorithm_orders, key=lambda x: len(algorithm_orders[x]))
best_algorithm_order = algorithm_orders[best_algorithm_name]

print("The best scheduling algorithm for this case is:", best_algorithm_name)
print("Order of patients for the best algorithm:", best_algorithm_order)
