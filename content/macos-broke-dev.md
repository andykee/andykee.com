Title: macOS upgrade broke my dev shit! 
Date: 2016-07-08
Tags: osx

After installing the macOS Sierra beta, I noticed git and homebrew weren't working anymore. The same thing happened when I upgraded to OSX El Cap. Moderately annoying, but simple to fix:

First, let's restore permissions on `/usr/local`:

    :::bash
    sudo chflags norestricted /usr/local && sudo chown $(whoami):admin /usr/local && sudo chown -R $(whoami):admin /usr/local

Next, we need to reinstall the Xcode developer tools:

    :::bash
    xcode-select --install

This fixes all the `xcrun` errors we get when trying to use any number of command line tools. Finally, make sure homebrew is happy:

    :::bash
    brew update
    brew doctor

That's it! Ez-pz.

