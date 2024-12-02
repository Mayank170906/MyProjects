import datetime
from datetime import datetime, timedelta
class CRICTIME:
    def remaining(self,hour_,minute_,second_,microsecond_):
        current_time = datetime.now()
        target_time = current_time.replace(hour=hour_, minute=minute_, second=second_, microsecond=microsecond_)
        if current_time > target_time:
            target_time += timedelta(days=1)
        remaining_time = target_time - current_time
        return remaining_time
