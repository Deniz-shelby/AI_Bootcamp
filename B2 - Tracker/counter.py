# the input is the column for anroid.sensor.accelerometer#mean and if the target is walking
#as output i need this array for the step counter
def step_counter_on_walking(accelerometer_mean_list_for_walking):
    
    step_counter = 0
    for i in range(len(accelerometer_mean_list_for_walking)-1):
        if i > 0:
            y = accelerometer_mean_list_for_walking[i]
            y_before = accelerometer_mean_list_for_walking[i-1]
            y_after = accelerometer_mean_list_for_walking[i+1]
            if (y > y_before) & (y> y_after) & (10 < (y_before+y_after)):
                step_counter +=1
    return step_counter

df['android.sensor.accelerometer#mean'] # but onyl for target walking

steps = step_counter_on_walking(acc_mean)
steps

def steps_to_meters(step_count):
    meters = step_count * 0.762
    return meters 

meters = steps_to_meters(steps)


# here duration in s implemented from vladimirs code

def pace_in_m_s(meters,duration_in_s):
    pace = meters/duration_in_s
    return pace



def pace_in_km_h(meters,duration_in_s):
    pace = (meters/1000)/(duration_in_s/360)
    return pace