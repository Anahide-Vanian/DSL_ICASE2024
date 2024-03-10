/*
 * generated by Xtext 2.32.0
 */
grammar DebugInternalBddDsl;

// Rule Model
ruleModel:
	'model'
	RULE_ID
	(
		ruleModelRef
		    |
		ruleDeclarativeEntityDef
		    |
		ruleImperativeEntityDef
		    |
		ruleScenario
	)*
;

// Rule ModelRef
ruleModelRef:
	'using'
	RULE_ID
;

// Rule DeclarativeEntityDef
ruleDeclarativeEntityDef:
	'declarative'
	'entity'
	(
		RULE_ID
		    |RULE_STRING
	)
	(
		'-'
		ruleWORD
	)?
	(
		'is'
		RULE_ID
		(
			','
			RULE_ID
		)*
	)?
	'{'
	(
		'actions:'
		ruleActionDef
		(
			','
			ruleActionDef
		)*
	)?
	(
		'states:'
		ruleStateDef
		ruleWORD?
		(
			ruleWORD
			'-'
			ruleWORD
		)?
		(
			(
				','
				    |
				'and'
				    |
				'the'
			)
			ruleStateDef
		)*
	)?
	(
		'properties:'
		rulePropertyDef
		ruleWORD?
		(
			ruleWORD
			'-'
			ruleWORD
		)?
		(
			(
				','
				    |
				'and'
				    |
				'the'
			)
			rulePropertyDef
		)*
	)?
	'}'
;

// Rule ImperativeEntityDef
ruleImperativeEntityDef:
	'imperative'
	'entity'
	(
		RULE_ID
		    |RULE_STRING
	)
	(
		'-'
		ruleWORD
	)?
	(
		'is'
		RULE_ID
		(
			','
			RULE_ID
		)*
	)?
	'{'
	(
		'actions:'
		ruleImperativeActionDef
		(
			','
			ruleImperativeActionDef
		)*
	)?
	(
		'states:'
		ruleImperativeStateDef
		ruleWORD?
		(
			ruleWORD
			'-'
			ruleWORD
		)?
		(
			(
				','
				    |
				'and'
				    |
				'the'
			)
			ruleImperativeStateDef
		)*
	)?
	(
		'properties:'
		ruleImperativePropertyDef
		ruleWORD?
		(
			ruleWORD
			'-'
			ruleWORD
		)?
		(
			(
				','
				    |
				'and'
				    |
				'the'
			)
			ruleImperativePropertyDef
		)*
	)?
	'}'
;

// Rule ImperativeActionDef
ruleImperativeActionDef:
	ruleWORD
	ruleWORD?
;

// Rule ActionDef
ruleActionDef:
	ruleWORD
	ruleWORD?
;

// Rule PREP
rulePREP:
	(
		'on'
		    |
		'in'
		    |
		'from'
		    |
		'to'
		    |
		'into'
		    |
		'for'
		    |
		'with'
	)
;

// Rule ADVERB
ruleADVERB:
	'linearly'
;

// Rule WORD
ruleWORD:
	RULE_ID
;

// Rule StateDef
ruleStateDef:
	ruleStateName
	rulePREP?
	(
		'/'
		ruleStateName
	)?
;

// Rule StateName
ruleStateName:
	ruleWORD
	(
		'and'
		ruleWORD
		    |
		'off'
		ruleWORD
	)?
;

// Rule PropertyDef
rulePropertyDef:
	ruleWORD
	'*'
	?
;

// Rule ImperativeStateDef
ruleImperativeStateDef:
	ruleImperativeStateName
	rulePREP?
	(
		'/'
		ruleImperativeStateName
	)?
;

// Rule ImperativeStateName
ruleImperativeStateName:
	ruleStateName
;

// Rule ImperativePropertyDef
ruleImperativePropertyDef:
	ruleWORD
	'*'
	?
;

// Rule ID_OR_STRING
ruleID_OR_STRING:
	(
		RULE_ID
		    |
		RULE_STRING
	)
;

// Rule ImperativeScenario
ruleImperativeScenario:
	'which'
	'means'
	'Given'
	ruleImperativeScenarioState
	'When'
	ruleImperativeScenarioAction
	'Then'
	ruleImperativeScenarioState
;

// Rule Scenario
ruleScenario:
	'Scenario:'
	ruleID_OR_STRING
	(
		'out'
		    |
		'off'
		    |
		'on'
		    |
		'in'
		    |
		'-'
		    |
		'the'
		    |
		'to'
		'the'
		    |
		'to'
	)?
	ruleWORD?
	(
		'off'
		    |
		'on'
		    |
		'in'
		    |
		'-'
		    |
		'the'
	)?
	ruleWORD?
	(
		'on'
		    |
		'in'
		    |
		'-'
		    |
		'the'
	)?
	ruleWORD?
	(
		'in'
		    |
		'-'
		    |
		'the'
	)?
	ruleWORD?
	(
		(
			'Given'
			'the'
			    |
			'Given'
			'I'
			    |
			'Given'
		)
		(
			'do'
			'not'
		)?
		ruleOPTION
		    |
		'Given'
		(
			'the'
			    |
			'all'
			'the'
			    |
			'I'
		)?
		(
			'do'
			'not'
		)?
		ruleDeclarativeScenarioState
	)
	ruleImperativeScenario
	?
	(
		(
			'When'
			'I'
			    |
			'When'
			'the'
			    |
			'When'
			    |
			'And'
			'I'
		)
		(
			'do'
			'not'
		)?
		ruleOPTION
		    |
		(
			'When'
			'I'
			    |
			'When'
			'I'
			'do'
			'not'
			    |
			'When'
			'the'
			    |
			'Given'
			'I'
			    |
			'When'
		)
		ruleDeclarativeScenarioAction
	)
	ruleImperativeScenario
	?
	(
		(
			'Then'
			'the'
			    |
			'Then'
			'I'
			    |
			'Then'
		)
		(
			'do'
			'not'
		)?
		ruleOPTION
		    |
		'Then'
		(
			'the'
			    |
			'all'
			'the'
			    |
			'I'
		)?
		(
			'do'
			'not'
		)?
		ruleDeclarativeScenarioState
	)
	ruleImperativeScenario
	?
;

// Rule DeclarativeScenarioState
ruleDeclarativeScenarioState:
	ruleDeclarativeStatePhrase
	(
		'And'
		ruleDeclarativeStatePhrase
	)*
;

// Rule ImperativeScenarioState
ruleImperativeScenarioState:
	ruleImperativeStatePhrase
	(
		'And'
		ruleImperativeStatePhrase
	)*
;

// Rule DeclarativeScenarioAction
ruleDeclarativeScenarioAction:
	ruleDeclarativeActionPhrase
	(
		'And'
		ruleDeclarativeActionPhrase
	)*
;

// Rule ImperativeScenarioAction
ruleImperativeScenarioAction:
	ruleImperativeActionPhrase
	(
		'And'
		ruleImperativeActionPhrase
	)*
;

// Rule DeclarativeStatePhrase
ruleDeclarativeStatePhrase:
	(
		ruleDeclarativeEntityPropertyStatePhrase
		    |
		ruleDeclarativeEntityStatePhrase
	)
;

// Rule ImperativeStatePhrase
ruleImperativeStatePhrase:
	(
		ruleImperativeEntityPropertyStatePhrase
		    |
		ruleImperativeEntityStatePhrase
	)
;

// Rule ENTITY_IDENTITY
ruleENTITY_IDENTITY:
	(
		'#'
		RULE_INT
		    |
		RULE_STRING
	)
;

// Rule OPTION
ruleOPTION:
	'#'?
	(
		RULE_INT
		    |
		RULE_STRING
	)
;

// Rule DeclarativeEntityRef
ruleDeclarativeEntityRef:
	(
		(
			ruleWORD
			ruleOPTION
			'for'
			'the'
		)?
		(
			'for'
			    |
			'of'
			    |
			'to'
		)?
		(
			'the'
			    |
			'all'
			'the'
		)
		ruleWORD
		ruleENTITY_IDENTITY
		    |
		ruleENTITY_IDENTITY
	)
;

// Rule ImperativeEntityRef
ruleImperativeEntityRef:
	'the'
	RULE_ID
	RULE_STRING
;

// Rule DeclarativeEntityStatePhrase
ruleDeclarativeEntityStatePhrase:
	(
		ruleWORD
		?
		(
			'of'
			    |
			'of'
			'the'
		)?
		ruleOPTION?
		(
			'for'
			    |
			'for'
			'the'
		)?
		(
			'of'
			    |
			'of'
			'the'
			    |
			'for'
			'the'
			    |
			'for'
		)
	)?
	ruleDeclarativeEntityRef
	(
		'is'
		    |
		'are'
	)
	'not'?
	RULE_ID
	ruleWORD?
;

// Rule ImperativeEntityStatePhrase
ruleImperativeEntityStatePhrase:
	ruleImperativeEntityRef
	'is'
	RULE_ID
;

// Rule DeclarativeEntityPropertyStatePhrase
ruleDeclarativeEntityPropertyStatePhrase:
	ruleWORD
	?
	(
		'of'
		    |
		'of'
		'the'
	)?
	ruleOPTION?
	(
		'of'
		    |
		'for'
		    |
		'from'
		    |
		'for'
		'the'
		    |
		'of'
		'the'
	)
	ruleDeclarativeEntityRef
	(
		(
			'is'
			    |
			'is'
			'not'
		)
		ruleSimpleValue
		ruleWORD?
		ruleWORD?
		    |
		(
			(
				'are'
				    |
				'are'
				'not'
			)
			ruleSimpleValue
			ruleWORD?
			    |
			(
				','
				ruleSimpleValue
			)*
		)
		ruleWORD?
	)
;

// Rule ImperativeEntityPropertyStatePhrase
ruleImperativeEntityPropertyStatePhrase:
	'the'
	RULE_ID
	(
		'of'
		    |
		'for'
	)
	ruleImperativeEntityRef
	'is'
	ruleStringValue
;

// Rule SimpleValue
ruleSimpleValue:
	(
		ruleIntValue
		    |
		ruleStringValue
		    |
		ruleDoubleValue
	)
;

// Rule StringValue
ruleStringValue:
	RULE_STRING
;

// Rule IntValue
ruleIntValue:
	RULE_INT
;

// Rule DoubleValue
ruleDoubleValue:
	ruleDOUBLE
;

// Rule DeclarativeActionPhrase
ruleDeclarativeActionPhrase:
	(
		ruleDeclarativeEntityAction
		    |
		ruleVerbAction
	)
;

// Rule ImperativeActionPhrase
ruleImperativeActionPhrase:
	ruleImperativeEntityAction
;

// Rule VerbAction
ruleVerbAction:
	ruleDeclarativeActionRef
	'and'?
	ruleWORD?
	'on'?
	(
		ruleWORD
		'-'
		ruleWORD
	)?
	(
		'for'
		'the'
		    |
		'the'
		    |
		'on'
		    |
		'to'
		'the'
	)?
	ruleDeclarativeEntityDef
	?
	(
		'on'
		    |
		'off'
		    |
		'in'
	)?
	ruleDeclarativeEntityRef
	(
		'on'
		    |
		'off'
		    |
		'in'
	)?
	(
		'of'
		    |
		'for'
		    |
		'for'
		'the'
		    |
		'of'
		'the'
	)?
	rulePREP?
	ruleDeclarativeEntityRef
	?
;

// Rule DeclarativeEntityAction
ruleDeclarativeEntityAction:
	ruleDeclarativeEntityRef
	RULE_ID
	(
		'to'
		'the'
	)?
	ruleDeclarativeEntityRef
	?
	rulePropertyRef
	?
;

// Rule ImperativeEntityAction
ruleImperativeEntityAction:
	ruleImperativeEntityRef
	ruleADVERB
	?
	RULE_ID
	ruleImperativePropertyRef
	?
;

// Rule PropertyRef
rulePropertyRef:
	'to'
	RULE_ID
	ruleStringValue
	(
		'with'
		ruleStringValue
		RULE_ID
	)?
;

// Rule ImperativePropertyRef
ruleImperativePropertyRef:
	'to'
	RULE_ID
	ruleStringValue
	(
		'with'
		ruleStringValue
		RULE_ID
	)?
;

// Rule DeclarativeActionRef
ruleDeclarativeActionRef:
	ruleWORD
	'on'?
	ruleSimpleValue
	?
	rulePREP
	?
	(
		(
			'the'
			    |
			'on'
		)
		ruleDeclarativeEntityDef
	)?
;

// Rule DOUBLE
ruleDOUBLE:
	RULE_INT
	'.'
	RULE_INT
;

RULE_ID : '^'? ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*;

RULE_INT : ('0'..'9')+;

RULE_STRING : ('"' ('\\' .|~(('\\'|'"')))* '"'|'\'' ('\\' .|~(('\\'|'\'')))* '\'');

RULE_ML_COMMENT : '/*' ( options {greedy=false;} : . )*'*/' {skip();};

RULE_SL_COMMENT : '//' ~(('\n'|'\r'))* ('\r'? '\n')? {skip();};

RULE_WS : (' '|'\t'|'\r'|'\n')+ {skip();};

RULE_ANY_OTHER : .;
