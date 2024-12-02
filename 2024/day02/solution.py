class reportlevels:
    def __init__(self, reportfile=None):
        self.report = []
        if reportfile is not None:
            self.save_report_data(reportfile)
    
    def save_report_data(self, reportfile):
        with open(reportfile, "r") as rfile:
            for line in rfile:
                self.report.append(list(map(int, line.split(' '))))
    
    def is_all_decreasing_levels(self, reportline):
        decreasing = None
        for level in range(len(reportline)-1):
            level_diff = reportline[level] - reportline[level+1] 
            if decreasing is None and level_diff > 0:
                decreasing = True
            if decreasing is None and level_diff < 0:
                return False
            if decreasing and level_diff < 0:
                return False
        return True

    def is_all_increasing_levels(self, reportline):
        increasing = None
        for level in range(len(reportline)-1):
            level_diff = reportline[level] - reportline[level+1] 
            if increasing is None and level_diff < 0:
                increasing = True
            if increasing is None and level_diff > 0:
                return False
            if increasing and level_diff > 0:
                return False
        return True
    def is_between_1_and_3(self, reportline):
        for level in range(len(reportline)-1):
            level_diff = abs(reportline[level] - reportline[level+1])
            if (level_diff >= 1 and level_diff <= 3) and self.tolerate <= 0:
                return False
            self.tolerate -= 1
            continue
        return True

    def is_report_safe(self, reportline, problem_dampener_enabled=False):
        if isinstance(reportline, str):
            reportline = list(map(int, reportline.split(' ')))
        self.tolerate = 1 if problem_dampener_enabled else 0
        # print(f"{self.is_all_decreasing_levels(reportline)=} or {self.is_all_increasing_levels(reportline)=}) and {self.is_between_1_and_3(reportline)=}")
        return (self.is_all_decreasing_levels(reportline) or self.is_all_increasing_levels(reportline)) and self.is_between_1_and_3(reportline)



if __name__ == "__main__":
    rl = reportlevels("input.txt")
    safe_reports = sum(bool(rl.is_report_safe(each_report))
                   for each_report in rl.report)
    print(safe_reports)
    safe_reports = sum(bool(rl.is_report_safe(each_report, problem_dampener_enabled=True))
                   for each_report in rl.report)
    print(safe_reports)
