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

## Contributing and formats
Contribute via pull requests a la [Sean Davis's 
awesome-single-cell](https://github.com/seandavi/awesome-single-cell).

In an attempt to standardize cell types and gene names, I will enforce the use
of Cell Ontology (CL) IDs for celltypes. Find CL IDs for cells at 
[the OLS][ols] or [Ontobee][ontobee].

Marker gene list formats are not finalized.  For the time being, the format
will consist of a single plain markdown file for each cell type with the below
formatting.  This allows easy viewing, copy/paste, and concatentation, as well 
as most dataframe parsers support easy parsing with `sep=' | '`. 

### Filename formating
File format is as follows:

    CL_ID.cell_type_name.md
    
For example, take [B cells (CL_0000236)][b-cell]:

    CL_0000236.b_cell.md
    
This is distinct from say a [mature B cell (CL_0000785)][mature-b-cell]:

    CL_0000785.mature_b_cell.md
    
Due to the hierarchical nature of the ontologies, any markers for mature B cells
are necessarily B cell markers, so when choosing where to add a marker gene, add
it as deep in the onotology as you are comfortable (and can hopefully substantiate).

### List formatting
The list itself will take the following **headerless** format, with one gene per 
line:

    Marker gene | Species | ENSGID | Comment | Reference (DOI/URL)

Taking B cells as an example again, I may add the following:

    # file: CL_0000875.b_cell.md
    MS4A1 | homo sapiens | ENSG00000156738 | | doi:10.1038/ncomms14049
    
A more complicated case might be monocytes:

    # file: CL_0001054.monocyte.md
    CD14 | homo sapiens | ENSG00000170458 | CD14 monocyte (CL_0001054)| doi:10.1038/nri3158
    FCGR3A | homo sapiens | ENSG00000203747 | CD16 monocyte (CL_0002396) | doi:10.1016/j.immuni.2010.09.007
    
If a certain subtype has some marker genes above some critical threshold yet 
to be determined we can then split it off into its own file.
    
Genes present in multiple species should be added one per line with the correct
ENSGID for that species.  I don't want to break species up into different files
because ultimately I'd like to learn relationships between species.

[1]: https://www.cell.com/pb-assets/consortium/pancanceratlas/pancani3/index.html
[2]: https://www.nature.com/articles/nmeth.4644
[3]: https://github.com/dviraran/SingleR
[ols]: https://www.ebi.ac.uk/ols/ontologies/cl
[ontobee]: http://www.ontobee.org/ontology/cl
[b-cell]: http://www.ontobee.org/ontology/CL?iri=http://purl.obolibrary.org/obo/CL_0000236
[mature-b-cell]: http://www.ontobee.org/ontology/CL?iri=http://purl.obolibrary.org/obo/CL_0000785
