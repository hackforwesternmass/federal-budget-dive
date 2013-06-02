federal-budget-dive
====================

What will be revealed in the bowels of the federal budget?


The `extractdata` program (a Python3 script) extracts the tablular
data from the Budget Appendix into a CSV file.  The columns are:

    agency-code     The `agency-code` attribute of the `agency` element.
    agency-name     The content of the first 'header' tag inside the `agency` element.
    bureau-code     The `bureau-code` attribute of the `bureau` element.
    bureau-name     The content of the first `header` tag inside the `bureau` element.
    account-code    The `account-code` attribute of the `account` element.  Genrally
                        the first four digets after the first hyphen of the
                        treasury-code.
    treasury-code   The `treasury-code` attribute of the `account` element.
    account-name    The content of the first `header` tag inside the `account` element.
    account-deleted The `account-deleted` attribute of the `account` element.  Appears
                        to always be 'N'.
    schedule-code   The `schedule-code` attribute of the `schedule` element.  Probably
                        an internal document ID, but appears to be unique.
    schedule-treasury-id The first line of each schedule table gives the full
                        treasury id...this is just the id portion of that line,
                        without the prefix text.
    schedule-name   The content of the `ttitle` element of the schedule table if
                        it has one.
    col3-head       The text of the column header for column 3 of the table.  This
                        text indicates the provenance of the data (whether it
                        is actual, estimated, continuing resolution, etc).
    col4-head       As col3, for column 4.
    col5-head       As col3, for column 5, but it may also be `NA` if the table
                        has no column 5.
    stub-hierarchy  The `stub-hierarchy` attribute of the table row.  Indiates the
                        level of indentation of the row within the table.
    row-num         Sequential index of the row within the table.
    col1            Table column 1.  Often contains a mysterious number whose
                        meaning we were not able to discover (except for the
                        'Object Classification` tables, where the ID is
                        explained in http://www.whitehouse.gov/sites/default/files/omb/budget/fy2014/assets/objclass.pdf
    col2            Description of the line entry.
    col3            Generally the 2011 actual data.
    col4            Generally the 2013 CR data.
    col5            Generally the 2014 estimated data.

`extractdata` also has a `--db` option which will also generate a set of
normalized csv files that can be uploaded into an sql database.  In these files
the accounts and schedules are given sequential id numbers to allow linking.
