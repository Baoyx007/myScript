# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import codecs
'''
485454502f312e3120323030204f4b0d0a5365727665723a2054656e67696e650d0a446174653a204672692c203038204d617920323031352030323a35313a303320474d540d0a436f6e74656e742d547970653a20746578742f68746d6c3b636861727365743d5554462d380d0a5472616e736665722d456e636f64696e673a206368756e6b65640d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a436f6e74656e742d456e636f64696e673a20677a69700d0a566172793a204163636570742d456e636f64696e670d0a43616368652d436f6e74726f6c3a20707269766174650d0a5365742d436f6f6b69653a20696435383d303563444e31564d4a4a637a6f4951794755354941673d3d3b20657870697265733d53756e2c2030372d4d61792d31372030323a35313a303320474d543b20646f6d61696e3d35382e636f6d3b20706174683d2f0d0a5033503a20706f6c6963797265663d222f7733632f7033702e786d6c222c2043503d224355522041444d204f5552204e4f5220535441204e4944220d0a0d0a64620d0a1f8b0800000000000000744fbd0ac230107e979b3b586915fa2ad22136d106daa43489a8a5e02882ee0547c1cd4dec03b505dfc24bece26086cb7d3fc97d57412613a219441570b19289a4d8c3c41df0a064ca64daaa09d73b8816304556a558baf6343c5f107b404a46ace407930085c26823f11e9ac7bb3958c3d228e5de86736b480da152ac55ca2941d89f2f5d7beddb637fbb435c7b2e88665b1c0b803027c55ecafc5fc40d2b159702291fd1d709fe0c7b4172eb1c837a407939526e01ca952622b1d80fdd573f83eb8f00010000ffff480dda941c0100000d0a300d0a0d0a
'''
str = '485454502f312e3120323030204f4b0d0a5365727665723a2054656e67696e650d0a446174653a204672692c203038204d617920323031352030323a35313a303320474d540d0a436f6e74656e742d547970653a20746578742f68746d6c3b636861727365743d5554462d380d0a5472616e736665722d456e636f64696e673a206368756e6b65640d0a436f6e6e656374696f6e3a206b6565702d616c6976650d0a436f6e74656e742d456e636f64696e673a20677a69700d0a566172793a204163636570742d456e636f64696e670d0a43616368652d436f6e74726f6c3a20707269766174650d0a5365742d436f6f6b69653a20696435383d303563444e31564d4a4a637a6f4951794755354941673d3d3b20657870697265733d53756e2c2030372d4d61792d31372030323a35313a303320474d543b20646f6d61696e3d35382e636f6d3b20706174683d2f0d0a5033503a20706f6c6963797265663d222f7733632f7033702e786d6c222c2043503d224355522041444d204f5552204e4f5220535441204e4944220d0a0d0a64620d0a1f8b0800000000000000744fbd0ac230107e979b3b586915fa2ad22136d106daa43489a8a5e02882ee0547c1cd4dec03b505dfc24bece26086cb7d3fc97d57412613a219441570b19289a4d8c3c41df0a064ca64daaa09d73b8816304556a558baf6343c5f107b404a46ace407930085c26823f11e9ac7bb3958c3d228e5de86736b480da152ac55ca2941d89f2f5d7beddb637fbb435c7b2e88665b1c0b803027c55ecafc5fc40d2b159702291fd1d709fe0c7b4172eb1c837a407939526e01ca952622b1d80fdd573f83eb8f00010000ffff480dda941c0100000d0a300d0a0d0a'
print(codecs.decode(str,'hex'))