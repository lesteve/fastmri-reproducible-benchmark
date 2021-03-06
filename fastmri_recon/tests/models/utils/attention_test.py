import tensorflow as tf

from fastmri_recon.models.utils.attention import ChannelAttentionBlock


def test_channel_attention_block_call():
    ca_block = ChannelAttentionBlock()
    inputs = tf.random.normal([2, 32, 32, 16])
    ca_block(inputs)
