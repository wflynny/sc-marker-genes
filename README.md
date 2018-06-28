# sc-marker-genes
This repository holds lists of genes that can be used to identify cell 
(sub-)types in single cell mRNA-seq experiments.

## Objective and goals
The current methodolgy for assigning a putative "cell type" or "subtype" 
to an individual cell involves (1) embedding cells into a low dimensional 
manifold using their high dimensional gene expression profiles, (2) 
clustering cells with similar low dimensional expression profiles together,
(3) extracting "marker" genes whose expression is limited to specific 
clusters or subclusters, and finally (4) associating a known cell 
(sub-)type to all cells in that cluster based on biological knowlege of 
those marker genes.

Each of the steps above (and several prior preprocessing steps) rely on 
thresholds, parameter tuning, and some level of biological insight. An 
alternative is to train a machine to identify the identity of a cell using
a large collection of already-labeled cells. Projects to construct such 
*classification* methods are underway or already exist for specific organs,
tissue types, or biological conditions, [[1]][[2]][[3]] as examples.

Training a *classifier* needs high quality cell (sub-)type representatives, 
and to amass such training data, robust cell (sub-)type candidates must first 
be identified by hand by the expression of marker genes specific to those cell 
(sub-)types.  The goal of this repository is to open/crowd-source marker genes 
which can be used to robustly identify cell types.

## Contributing and format
Contribute via pull requests a la [Sean Davis's 
awesome-single-cell](https://github.com/seandavi/awesome-single-cell).

Marker gene list formats are not finalized.  For the time being, the format
consist of a single plain markdown file for each cell type with the following
**headerless** format:

    Marker gene | Subtype or other annotation for cell type | Reference

This allows easy viewing, copy/paste, and concatentation, as well as most 
dataframe parsers support easy parsing with `sep='|'`. 

[1]: https://www.cell.com/pb-assets/consortium/pancanceratlas/pancani3/index.html
[2]: https://www.nature.com/articles/nmeth.4644
[3]: https://github.com/dviraran/SingleR
