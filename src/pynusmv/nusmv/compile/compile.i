%module(package="pynusmv.nusmv.compile") compile

%{
#include "../../../nusmv/nusmv-config.h"
#include "../../../nusmv/src/utils/defs.h"
#include "../../../nusmv/src/compile/compile.h" 
#include "../../../nusmv/src/compile/FlatHierarchy.h" 
#include "../../../nusmv/src/compile/PredicateExtractor.h" 
#include "../../../nusmv/src/compile/PredicateNormaliser.h" 
%}

# Removing possible memory leak warning.
# Pointer to global flat hierarchy has to be cautiously used.
#pragma SWIG nowarn=454

# Ignoring unimplemented functions
%ignore Compile_BuildVarsBdd;
%ignore build_proc_selector;
%ignore Compile_CompileInit;
%ignore Compile_CompileModel;
%ignore lookup_param_hash;
%ignore print_conjunctive_partition_info;
%ignore Compile_BuildInitBdd;
%ignore Compile_BuildInvarBdd;
%ignore start_test;
%ignore end_test;

%feature("autodoc", 1);

%include ../typedefs.tpl

%include ../../../nusmv/src/utils/defs.h
%include ../../../nusmv/src/compile/compile.h
%include ../../../nusmv/src/compile/FlatHierarchy.h
%include ../../../nusmv/src/compile/PredicateExtractor.h
%include ../../../nusmv/src/compile/PredicateNormaliser.h

%inline %{

int compile_flatten_smv(boolean calc_vars_constrains);

// TODO Remove this?
EXTERN FlatHierarchy_ptr mainFlatHierarchy;
EXTERN cmp_struct_ptr cmps;


struct cmp_struct {
  int      read_model;
  int      hrc_built;
  int      flatten_hierarchy;
  int      encode_variables;
  int      process_selector;
  int      build_frames;
  int      build_model;
  int      build_flat_model;
  int      build_bool_model;
  int      bmc_init;
  int      bmc_setup;
  int      fairness_constraints;
  int      coi;
};

void cmp_struct_reset(cmp_struct_ptr cmp) {
    cmp->read_model           = 0;
    cmp->hrc_built            = 0;
    cmp->flatten_hierarchy    = 0;
    cmp->encode_variables     = 0;
    cmp->process_selector     = 0;
    cmp->build_frames         = 0;
    cmp->build_model          = 0;
    cmp->build_flat_model     = 0;
    cmp->build_bool_model     = 0;
    cmp->bmc_init             = 0;
    cmp->bmc_setup            = 0;
    cmp->fairness_constraints = 0;
    cmp->coi                  = 0;
}

%}