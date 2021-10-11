%apache% --start
%mda2sql% init.mda
%mysql% --start
%chrome% --wait "localhost"
%apache% --stop
%mysql% --stop
