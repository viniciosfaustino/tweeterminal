#!/bin/sh

function tweeterminal()
{
  conda run -n tweeterminal python /opt/tweeterminal/tweeterminal.py $@
}
