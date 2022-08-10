#!/bin/sh
echo "Converting notebooks..."
make convert
echo "Restart Jekyll..."
make restart-jekyll
wait
echo "Finished"