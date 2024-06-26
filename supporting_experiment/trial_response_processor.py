from globals import *
from psychopy import event

from supporting_experiment.sounds import Sounds


class TrialResponseProcessor:
    """
    The TrialResponseProcessor class is responsible for processing the responses of the participant in each trial.
    """

    def __init__(self):
        self.accu = 0
        self.response_list = []

    def reset(self):
        """
        Resets the accuracy counter.
        """

        self.accu = 0

    def process(self, trial, trial_i, correct_answer):
        """
        Processes the response of the participant in a trial.

        :param trial: the trial number
        :param trial_i: the trial index
        :param correct_answer: the correct answer for each trial
        """

        response = event.getKeys(keyList=['f', 'j'])
        self.response_list.append(response)

        # Record RT & keyboard responses
        timeee = config_exp.timer.getTime()

        if len(self.response_list[trial_i]) == 0:
            self.response_list[trial_i].append("miss")

        sounds = Sounds()

        # Auditory feedback on trial accuracy
        # Note that parallel_ports.port_write.setData() is not used in the current study
        if self.response_list[trial_i][0] == correct_answer[trial]:
            #if parallel_ports.use:
                #parallel_ports.port_write.setData(6)
            sounds.correct_sound.play()
            self.accu += 1
        elif (self.response_list[trial_i][0] != correct_answer[trial]) and (correct_answer[trial] == "miss"):
            #if parallel_ports.use:
                #parallel_ports.port_write.setData(7)
            sounds.fail_to_stop_sound.play()
        else:
            #if parallel_ports.use:
                #parallel_ports.port_write.setData(8)
            sounds.incorrect_sound.play()
