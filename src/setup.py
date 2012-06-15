import os.path
from distutils.core import setup
from distutils.extension import Extension

abspath = os.path.abspath('.')
include_dirs = ['nusmv', 'nusmv/src', 'cudd-2.4.1.1/include']
swig_opts = ['-py3']
libraries = ['nusmv']
library_dirs = [os.path.join(abspath,'lib')]
extensions = []

# addons_core modules
extensions.append(
	Extension('pynusmv.nusmv.addons_core._addons_core',
				['pynusmv/nusmv/addons_core/addons_core.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/addons_core/addonsCore.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.addons_core.compass._compass',
				['pynusmv/nusmv/addons_core/compass/compass.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/addons_core/compass/compass.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.addons_core.compass.compile._compile',
				['pynusmv/nusmv/addons_core/compass/compile/compile.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/addons_core/compass/compile/ProbAssign.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.addons_core.compass.parser.ap._ap',
				['pynusmv/nusmv/addons_core/compass/parser/ap/ap.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/addons_core/compass/parser/ap/ap_grammar.h',
							'nusmv/src/addons_core/compass/parser/ap/ParserAp.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.addons_core.compass.parser.prob._prob',
				['pynusmv/nusmv/addons_core/compass/parser/prob/prob.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/addons_core/compass/parser/prob/ParserProb.h',
							'nusmv/src/addons_core/compass/parser/prob/prob_grammar.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# be module
extensions.append(
	 Extension('pynusmv.nusmv.be._be',
				['pynusmv/nusmv/be/be.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/be/be.h',
							'nusmv/src/be/bePkg.h',
							'nusmv/src/be/beRbcManager.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)

# bmc modules
extensions.append(
	 Extension('pynusmv.nusmv.bmc._bmc',
				['pynusmv/nusmv/bmc/bmc.i'],
				depends = [	'nusmv/src/utils/defs.h',
							'nusmv/src/bmc/bmc.h',
							'nusmv/src/bmc/bmcBmc.h',
							'nusmv/src/bmc/bmcCheck.h',
							'nusmv/src/bmc/bmcCmd.h',
							'nusmv/src/bmc/bmcConv.h',
							'nusmv/src/bmc/bmcDump.h',
							'nusmv/src/bmc/bmcGen.h',
							'nusmv/src/bmc/bmcModel.h',
							'nusmv/src/bmc/bmcPkg.h',
							'nusmv/src/bmc/bmcSimulate.h',
							'nusmv/src/bmc/bmcTableau.h',
							'nusmv/src/bmc/bmcUtils.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.bmc.sbmc._sbmc',
				['pynusmv/nusmv/bmc/sbmc/sbmc.i'],
				depends = [	'nusmv/src/utils/defs.h',
							'nusmv/src/bmc/sbmc/sbmcBmc.h',
							'nusmv/src/bmc/sbmc/sbmcBmcInc.h',
							'nusmv/src/bmc/sbmc/sbmcCmd.h',
							'nusmv/src/bmc/sbmc/sbmcGen.h',
							'nusmv/src/bmc/sbmc/sbmcHash.h',
							'nusmv/src/bmc/sbmc/sbmcNodeStack.h',
							'nusmv/src/bmc/sbmc/sbmcPkg.h',
							'nusmv/src/bmc/sbmc/sbmcStructs.h',
							'nusmv/src/bmc/sbmc/sbmcTableau.h',
							'nusmv/src/bmc/sbmc/sbmcTableauInc.h',
							'nusmv/src/bmc/sbmc/sbmcTableauIncLTLformula.h',
							'nusmv/src/bmc/sbmc/sbmcTableauLTLformula.h',
							'nusmv/src/bmc/sbmc/sbmcUtils.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# cinit module
extensions.append(
	 Extension('pynusmv.nusmv.cinit._cinit',
				['pynusmv/nusmv/cinit/cinit.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/cinit/cinit.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# cmd module
extensions.append(
	 Extension('pynusmv.nusmv.cmd._cmd',
				['pynusmv/nusmv/cmd/cmd.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/cmd/cmd.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# compile modules
extensions.append(
	 Extension('pynusmv.nusmv.compile._compile',
				['pynusmv/nusmv/compile/compile.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/compile/compile.h',
							'nusmv/src/compile/FlatHierarchy.h',
							'nusmv/src/compile/PredicateExtractor.h',
							'nusmv/src/compile/PredicateNormaliser.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.compile.symb_table._symb_table',
				['pynusmv/nusmv/compile/symb_table/symb_table.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/compile/symb_table/NFunction.h',
							'nusmv/src/compile/symb_table/ResolveSymbol.h',
							'nusmv/src/compile/symb_table/symb_table.h',
							'nusmv/src/compile/symb_table/SymbCache.h',
							'nusmv/src/compile/symb_table/SymbLayer.h',
							'nusmv/src/compile/symb_table/SymbTable.h',
							'nusmv/src/compile/symb_table/SymbType.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.compile.type_checking._type_checking',
				['pynusmv/nusmv/compile/type_checking/type_checking.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/compile/type_checking/TypeChecker.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.compile.type_checking.checkers._checkers',
				['pynusmv/nusmv/compile/type_checking/checkers/checkers.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/compile/type_checking/checkers/CheckerBase.h',
							'nusmv/src/compile/type_checking/checkers/CheckerCore.h',
							'nusmv/src/compile/type_checking/checkers/CheckerPsl.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# dag module
extensions.append(
	 Extension('pynusmv.nusmv.dag._dag',
				['pynusmv/nusmv/dag/dag.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/dag/dag.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# dd module
extensions.append(
	 Extension('pynusmv.nusmv.dd._dd',
				['pynusmv/nusmv/dd/dd.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/dd/dd.h',
							'nusmv/src/dd/VarsHandler.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# enc modules
extensions.append(
	 Extension('pynusmv.nusmv.enc._enc',
				['pynusmv/nusmv/enc/enc.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/enc/enc.h',
							'nusmv/src/enc/operators.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.enc.base._base',
				['pynusmv/nusmv/enc/base/base.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/enc/base/BaseEnc.h',
							'nusmv/src/enc/base/BoolEncClient.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.enc.bdd._bdd',
				['pynusmv/nusmv/enc/bdd/bdd.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/enc/bdd/bdd.h',
							'nusmv/src/enc/bdd/BddEnc.h',
							'nusmv/src/enc/bdd/BddEncCache.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.enc.be._be',
				['pynusmv/nusmv/enc/be/be.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/enc/be/BeEnc.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.enc.bool._bool',
				['pynusmv/nusmv/enc/bool/bool.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/enc/bool/BitValues.h',
							'nusmv/src/enc/bool/BoolEnc.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.enc.utils._utils',
				['pynusmv/nusmv/enc/utils/utils.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/enc/utils/AddArray.h',
							'nusmv/src/enc/utils/OrdGroups.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# fsm modules
extensions.append(
	 Extension('pynusmv.nusmv.fsm._fsm',
				['pynusmv/nusmv/fsm/fsm.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/fsm/fsm.h',
							'nusmv/src/fsm/FsmBuilder.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.fsm.bdd._bdd',
				['pynusmv/nusmv/fsm/bdd/bdd.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/fsm/bdd/bdd.h',
							'nusmv/src/fsm/bdd/BddFsm.h',
							'nusmv/src/fsm/bdd/FairnessList.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.fsm.be._be',
				['pynusmv/nusmv/fsm/be/be.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/fsm/be/BeFsm.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.fsm.sexp._sexp',
				['pynusmv/nusmv/fsm/sexp/sexp.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/fsm/sexp/BoolSexpFsm.h',
							'nusmv/src/fsm/sexp/Expr.h',
							'nusmv/src/fsm/sexp/sexp.h',
							'nusmv/src/fsm/sexp/SexpFsm.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# hrc modules
extensions.append(
	 Extension('pynusmv.nusmv.hrc._hrc',
				['pynusmv/nusmv/hrc/hrc.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/hrc/hrc.h',
							'nusmv/src/hrc/hrcCmd.h',
							'nusmv/src/hrc/HrcFlattener.h',
							'nusmv/src/hrc/HrcNode.h',
							'nusmv/src/hrc/hrcPrefixUtils.h',
							'nusmv/src/hrc/HrcVarDependencies.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.hrc.dumpers._dumpers',
				['pynusmv/nusmv/hrc/dumpers/dumpers.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/hrc/dumpers/HrcDumper.h',
							'nusmv/src/hrc/dumpers/HrcDumperDebug.h',
							'nusmv/src/hrc/dumpers/HrcDumperSmv.h',
							'nusmv/src/hrc/dumpers/HrcDumperXml.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# ltl modules
extensions.append(
	 Extension('pynusmv.nusmv.ltl._ltl',
				['pynusmv/nusmv/ltl/ltl.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/ltl/ltl.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.ltl.ltl2smv._ltl2smv',
				['pynusmv/nusmv/ltl/ltl2smv/ltl2smv.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/ltl/ltl2smv/ltl2smv.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# mc module
extensions.append(
	 Extension('pynusmv.nusmv.mc._mc',
				['pynusmv/nusmv/mc/mc.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/mc/mc.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# node modules
extensions.append(
	 Extension('pynusmv.nusmv.node._node',
				['pynusmv/nusmv/node/node.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/node/MasterNodeWalker.h',
							'nusmv/src/node/node.h',
							'nusmv/src/node/NodeWalker.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.node.normalizers._normalizers',
				['pynusmv/nusmv/node/normalizers/normalizers.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/node/normalizers/MasterNormalizer.h',
							'nusmv/src/node/normalizers/NormalizerBase.h',
							'nusmv/src/node/normalizers/NormalizerCore.h',
							'nusmv/src/node/normalizers/NormalizerPsl.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.node.printers._printers',
				['pynusmv/nusmv/node/printers/printers.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/node/printers/MasterPrinter.h',
							'nusmv/src/node/printers/PrinterBase.h',
							'nusmv/src/node/printers/PrinterIWffCore.h',
							'nusmv/src/node/printers/PrinterPsl.h',
							'nusmv/src/node/printers/PrinterSexpCore.h',
							'nusmv/src/node/printers/PrinterWffCore.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# opt module
extensions.append(
	 Extension('pynusmv.nusmv.opt._opt',
				['pynusmv/nusmv/opt/opt.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/opt/opt.h',
							'nusmv/src/opt/OptsHandler.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# parser modules
extensions.append(
	 Extension('pynusmv.nusmv.parser._parser',
				['pynusmv/nusmv/parser/parser.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/node/node.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/parser/grammar.h',
							'nusmv/src/parser/parser.h',
							'nusmv/src/parser/symbols.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.parser.idlist._idlist',
				['pynusmv/nusmv/parser/idlist/idlist.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/node/node.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/parser/idlist/idlist_grammar.h',
							'nusmv/src/parser/idlist/ParserIdList.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.parser.ord._ord',
				['pynusmv/nusmv/parser/ord/ord.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/node/node.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/parser/ord/ord_grammar.h',
							'nusmv/src/parser/ord/ParserOrd.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.parser.psl._psl',
				['pynusmv/nusmv/parser/psl/psl.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/node/node.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/parser/psl/psl_grammar.h',
							'nusmv/src/parser/psl/psl_symbols.h',
							'nusmv/src/parser/psl/pslExpr.h',
							'nusmv/src/parser/psl/pslNode.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# prop module
extensions.append(
	 Extension('pynusmv.nusmv.prop._prop',
				['pynusmv/nusmv/prop/prop.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/prop/Prop.h',
							'nusmv/src/prop/PropDb.h',
							'nusmv/src/prop/propPkg.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)

# rbc modules
extensions.append(
	 Extension('pynusmv.nusmv.rbc._rbc',
				['pynusmv/nusmv/rbc/rbc.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/rbc/ConjSet.h',
							'nusmv/src/rbc/InlineResult.h',
							'nusmv/src/rbc/rbc.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.rbc.clg._clg',
				['pynusmv/nusmv/rbc/clg/clg.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/rbc/clg/clg.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# sat module
extensions.append(
	 Extension('pynusmv.nusmv.sat._sat',
				['pynusmv/nusmv/sat/sat.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/sat/sat.h',
							'nusmv/src/sat/SatIncSolver.h',
							'nusmv/src/sat/SatSolver.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# set module
extensions.append(
	 Extension('pynusmv.nusmv.set._set',
				['pynusmv/nusmv/set/set.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/set/set.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# sexp module
extensions.append(
	 Extension('pynusmv.nusmv.sexp._sexp',
				['pynusmv/nusmv/sexp/sexp.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/sexp/SexpInliner.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# simulate module
extensions.append(
	 Extension('pynusmv.nusmv.simulate._simulate',
				['pynusmv/nusmv/simulate/simulate.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/simulate/simulate.h',
							'nusmv/src/simulate/simulateTransSet.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)

# trace modules
extensions.append(
	 Extension('pynusmv.nusmv.trace._trace',
				['pynusmv/nusmv/trace/trace.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/trace/pkg_trace.h',
							'nusmv/src/trace/Trace.h',
							'nusmv/src/trace/TraceLabel.h',
							'nusmv/src/trace/TraceManager.h',
							'nusmv/src/trace/TraceOpt.h',
							'nusmv/src/trace/TraceXml.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trace.eval._eval',
				['pynusmv/nusmv/trace/eval/eval.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/trace/eval/BaseEvaluator.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trace.exec._exec',
				['pynusmv/nusmv/trace/exec/exec.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/trace/exec/BaseTraceExecutor.h',
							'nusmv/src/trace/exec/BDDCompleteTraceExecutor.h',
							'nusmv/src/trace/exec/BDDPartialTraceExecutor.h',
							'nusmv/src/trace/exec/CompleteTraceExecutor.h',
							'nusmv/src/trace/exec/PartialTraceExecutor.h',
							'nusmv/src/trace/exec/SATCompleteTraceExecutor.h',
							'nusmv/src/trace/exec/SATPartialTraceExecutor.h',
							'nusmv/src/trace/exec/traceExec.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trace.loaders._loaders',
				['pynusmv/nusmv/trace/loaders/loaders.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/trace/loaders/TraceLoader.h',
							'nusmv/src/trace/loaders/TraceXmlLoader.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trace.plugins._plugins',
				['pynusmv/nusmv/trace/plugins/plugins.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/trace/plugins/TraceCompact.h',
							'nusmv/src/trace/plugins/TraceExplainer.h',
							'nusmv/src/trace/plugins/TracePlugin.h',
							'nusmv/src/trace/plugins/TraceTable.h',
							'nusmv/src/trace/plugins/TraceXmlDumper.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)	

# trans modules
extensions.append(
	 Extension('pynusmv.nusmv.trans._trans',
				['pynusmv/nusmv/trans/trans.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/trans/trans.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trans.bdd._bdd',
				['pynusmv/nusmv/trans/bdd/bdd.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/trans/bdd/bdd.h',
							'nusmv/src/trans/bdd/BddTrans.h',
							'nusmv/src/trans/bdd/Cluster.h',
							'nusmv/src/trans/bdd/ClusterList.h',
							'nusmv/src/trans/bdd/ClusterOptions.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.trans.generic._generic',
				['pynusmv/nusmv/trans/generic/generic.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/trans/generic/GenericTrans.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# utils module
extensions.append(
	 Extension('pynusmv.nusmv.utils._utils',
				['pynusmv/nusmv/utils/utils.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/utils/utils.h',
							'nusmv/src/utils/array.h',
							'nusmv/src/utils/assoc.h',
							'nusmv/src/utils/avl.h',
							'nusmv/src/utils/error.h',
							'nusmv/src/utils/heap.h',
							'nusmv/src/utils/list.h',
							'nusmv/src/utils/NodeGraph.h',
							'nusmv/src/utils/NodeList.h',
							'nusmv/src/utils/object.h',
							'nusmv/src/utils/Olist.h',
							'nusmv/src/utils/Pair.h',
							'nusmv/src/utils/portability.h',
							'nusmv/src/utils/range.h',
							'nusmv/src/utils/Slist.h',
							'nusmv/src/utils/Sset.h',
							'nusmv/src/utils/Stack.h',
							'nusmv/src/utils/TimerBench.h',
							'nusmv/src/utils/Triple.h',
							'nusmv/src/utils/ucmd.h',
							'nusmv/src/utils/ustring.h',
							'nusmv/src/utils/utils_io.h',
							'nusmv/src/utils/WordNumber.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
	
# wff modules
extensions.append(
	 Extension('pynusmv.nusmv.wff._wff',
				['pynusmv/nusmv/wff/wff.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/wff/wff.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)
extensions.append(
	 Extension('pynusmv.nusmv.wff.w2w._w2w',
				['pynusmv/nusmv/wff/w2w/w2w.i'],
				depends = [	'nusmv/nusmv-config.h',
							'nusmv/src/utils/defs.h',
							'nusmv/src/wff/w2w/w2w.h',
							'lib/libnusmv.so'],
				swig_opts = swig_opts, libraries = libraries,
				library_dirs = library_dirs, include_dirs = include_dirs)
	)


setup(	name = "PyNuSMV",
		version = "0.1.0",
		author = "Simon Busard",
		author_email = "simon.busard@uclouvain.be",
		url = "http://lvl.info.ucl.ac.be/",
		description = "Python interface for NuSMV.",
		ext_modules = extensions)