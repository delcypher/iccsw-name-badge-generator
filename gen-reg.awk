#!/usr/bin/awk -f
#
# This is a simple awk script to extract the necessary
# data for a csv file exported from Eventbrite for ICCSW'14
#
# Run like:
# $ ./gen-reg.awk < report-20140923-103100.csv
#
BEGIN { FS=","; count=0 }
{
    # Skip the first line
    if (NR > 1) {
        print $2","$3","$6 ; count++
    }
}
# This ensures we always have an even number of entries by adding a dummy entry if necessary
END {
    if (count % 2 != 0) {
        print "surname,first_name,dummy_card"
    }
}
