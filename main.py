from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6  # Hz
sdr.bandwidth = 2e6  # Hz
sdr.gain = 5

samples = sdr.read_samples(500)

print(samples)
