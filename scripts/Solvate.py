#!/usr/bin/env python
#
# Solvate models which have been through MD equilibration with implicit solvent
#
# Daniel L. Parton <partond@mskcc.org> - 21 Mar 2014
#

import MSMSeeder
import MSMSeeder.refinement

# ========
# Parse command-line arguments
# ========

import argparse
argparser = argparse.ArgumentParser(description='Models a set of target sequences onto a set of template structures using Modeller.', formatter_class=argparse.RawTextHelpFormatter)

argparser.add_argument('--ProcessOnlyTheseTargets', nargs='+', help='Supply one or more target IDs separated by spaces (e.g. "ABL1_HUMAN_D0")')
argparser.add_argument('--ProcessOnlyTheseTemplates', nargs='+', help='Supply one or more template IDs separated by spaces (e.g. "ABL1_HUMAN_D0_1OPL_A")')
args = argparser.parse_args()

MSMSeeder.core.check_project_toplevel_dir()

# ========
# Parse project metadata
# ========

project_metadata = MSMSeeder.core.ProjectMetadata()
project_metadata.load(MSMSeeder.core.project_metadata_filename)

# ========
# Solvate
# ========

MSMSeeder.refinement.solvate_models(process_only_these_targets=args.ProcessOnlyTheseTargets, process_only_these_templates=args.ProcessOnlyTheseTemplates)

# ========
# Determine distribution of nwaters and filter out those above the 68th percentile
# ========

MSMSeeder.refinement.determine_nwaters(process_only_these_targets=args.ProcessOnlyTheseTargets, process_only_these_templates=args.ProcessOnlyTheseTemplates)
