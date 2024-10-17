# %%

import panel as pn
pn.extension()

# %%
import pandas as pd
df = pd.DataFrame({'a':range(10), 'b':[chr(ord('A')+i) for i in range(10)]})
pn.extension("tabulator", inline=True)
tbl = pn.widgets.Tabulator(df,   #df is already defined before
                           show_index=False,
                           sizing_mode = 'stretch_width',
                          )
tbl

# %%
tbl
# %%