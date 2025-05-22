# Game Overview

This is a side-scrolling, top-view SRPG combined with roguelike elements. Players control a 4-character squad through strategic battles that emphasize terrain usage, unit synergy, and behavioral decision-making.

## Stage & Combat Flow

- Stage-based battles (20 minutes+)
- Temporary upgrades per stage:
  - Health, Mana, HP Regen, MP Regen
  - Flat Heal, Attack Power, MP Increase
  - Active Items (temporary boost), Debuffs, Buffs
- Reinforced enemies give better rewards

## Combat Rules

- Only one unit is possessed at a time; can be swapped (with cooldown)
- Each unit uses:
  - 1 Main Skill (active)
  - 1 Passive Skill (passive)
- Skills level up across the game (based on EXP & gold)
- Early-game skills are more reliable, late-game skills are situational
- Skill progression affects:
  - Power, Cooldown, Mana cost, Range, AoE, Effect

## Skill Target Types

- Targeted (e.g. click-to-hit)
- Non-targeted (AoE, dash, line)

## Terrain Elements

- Bush: Concealment, ambush
- Cover: Damage mitigation
- Aura Zone: Buffs when standing on it

## Unit Roles

### Tank

- Absorbs damage, stands at the front
- High durability, threat generation (aggro)

### Dealer

- High damage (physical or magic)
- May require support due to fragility

### Healer

- Heals allies and provides sustain
- Can generate high aggro from burst healing

### Supporter

- Buffs allies, reduces enemy efficiency
- May manipulate terrain or debuff enemies

## Unit Attributes

Each unit has the following stats:

- Movement Speed
- Health
- Mana
- Attack Range
- Attack Power
- Magic Power
- Passive (skill reference)
- Main Skill (skill reference)
- Critical Rate
- Critical Damage
- Final Damage Modifier
- Magic Resistance
- Armor
- Durability
- Aggro Score (increases with DPS / Healing / Buffing)

## Formation Rules

Formations must be followed during battle.

### Examples:

#### Default

- Tank | Dealer | Healer | Support

#### Damage Heavy

- Dealer | Dealer | Dealer | Healer

#### Tactical

- Tank | Support | Support | Healer

### Formation Logic

- Tanks are always in front
- Allies move based on speed, while preserving formation
- Some styles prioritize:
  - **Ambush**: Flank via bush
  - **Focus Fire**: All units hit the tank's target
  - **Solo Combat**: Spread out, act individually
