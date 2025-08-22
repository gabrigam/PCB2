
https://www.reddit.com/r/RTLSDR/comments/1bixs2e/rtlsdr_v4_static_on_linux_latest_raspberry_os_on/?rdt=44845


Hey, I solved this. It's a driver's issue. Installing GQRX updates some rtlsdr packages, interfeiring with the V4 driver previously installed. (Actually, without the driver it does recieve signal, but has an aprox. 40 MHz down offset). So these are the steps that worked for me: 

*Install the V4 drivers www.rtl-sdr.com/v4 

*Execute this command: sudo apt-mark hold rtl-sdr librtlsdr0 librtlsdr-dev (I don't really know if those three packages are necessary to hold, but at least the rtlsdr0 is crucial) 

*Install gr-osmosdr from source https://github.com/Nuand/gr-osmosdr (This was the package responsible for the rtlsdr0 updating) 

* Install GQRX from source https://www.gqrx.dk/download/gqrx-sdr-for-the-raspberry-pi  And that's all. (Sorry for my not very good english).