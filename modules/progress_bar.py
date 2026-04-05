from math import floor;
from datetime import datetime

class Progress():
    """
    An object that tracks and displays progress of ongoing tasks.

    Tasks - total integer amount of tracked tasks.
    Timestamps - a list of integers ranging from 0 to 100 in an ascending order.
    They represent the intervals at which the timestamp will be printed.
    By default, timestamps will be printed at 0%, 25%, 50%, 75% and 100% of progress completion.

    Progress - An integer ranging from 0 to 100. It represents the current stage of progress.
    Advance Progress() - advances current progress by 1 task.
    Current - An integer that represents latest finished task.
    Summary - A flag, that displays verbose time summary.
    Finished - A flag, that represents whether all tasks were performed or not.
    Start - A date of this object's creation.
    End - A date of flagging this object as finished.
    Update Progress(x) - sets current progress to Xth task. X is an integer and is expected to be a lesser number than total amount of tasks.
    """
    def __init__(self, tasks=100, timestamps=[0, 25, 50, 75, 100], summary=False):
        self.__timestamps = timestamps;
        self.__timestamps_remaining_idx = [x for x in range(len(timestamps))];
        self.__tasks = tasks;
        self.__summary = summary;
        self.__current = 0;
        
        self.start = datetime.now();
        self.end = None;
        self.finished = False;
        self.__update_progress(0);

    def advance_progress(self):
        self.__current += 1;
        self.__update_progress(self.__current);

    def __update_progress(self, new_value):
        if self.finished:
            return;

        self.progress = floor((new_value / self.__tasks) * 100);

        timestamp = self.__timestamps[self.__timestamps_remaining_idx[0]];
        if (self.progress >= timestamp):
            self.__timestamps_remaining_idx.pop(0);    
            print(str(timestamp) + '% ', datetime.now().time());

            if self.__timestamps_remaining_idx == []:
                    self.__finish();
        return timestamp;

    def __finish(self):
        self.finished = True;
        self.end = datetime.now();

        if (self.__summary):
            total_secs = (self.end - self.start).total_seconds()
            mins, secs = divmod(total_secs, 60);
            hrs, mins = divmod(mins, 60);
            print('processing took {} hours, {} minutes and {} seconds'.format(int(hrs), int(mins), int(secs)));