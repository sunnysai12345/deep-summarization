from tensorflow.models.rnn import rnn_cell
from models.stacked_bidirectional import StackedBidirectional


class GruStackedBidirectional(StackedBidirectional):
    def __init__(self,review_summary_file, checkpointer, num_layers, attention = False):
        """

        :param review_summary_file:
        :param checkpointer:
        :param attention:
        """
        self.num_layers = num_layers
        StackedBidirectional.__init__(self, review_summary_file, checkpointer, attention)

    def get_cell(self):
        """

        :return:
        """
        return rnn_cell.GRUCell(self.memory_dim)
