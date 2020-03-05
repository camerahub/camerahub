#!/usr/bin/perl -w

# This script generates SVG icons with the right names
# from the raw SVG icons obtained from Icons8

use strict;
use warnings;
use File::Copy;

# Set up mappings between old and new icon names. One source SVG can be mapped to multiple destination SVGs
my %newnames = (
	'icons8-camera-addon'			=> ['accessory'],
	'icons8-collectibles'			=> ['archive'],
	'icons8-battery'				=> ['battery'],
	'icons8-film-reel'				=> ['bulkfilm'],
	'icons8-cameras'				=> ['cameramodel'],
	'icons8-camera'					=> ['camera'],
	'icons8-camera-identification'	=> ['condition'],
	'icons8-volume'					=> ['developer'],
	'icons8-industrial-scales'		=> ['enlarger'],
	'icons8-easel'					=> ['exhibition'],
	'icons8-medium-icons'			=> ['exposureprogram'],
	'icons8-film-roll'				=> ['film', 'filmstock'],
	'icons8-360-degrees'			=> ['filter'],
	'icons8-camera-flash'			=> ['flash'],
	'icons8-connected-no-data'		=> ['flashprotocol'],
	'icons8-resolution'				=> ['format'],
	'icons8-lens'					=> ['lens', 'lensmodel'],
	'icons8-factory'				=> ['manufacturer'],
	'icons8-slr-small-lens'			=> ['mount'],
	'icons8-metamorphose'			=> ['mountadapter'],
	'icons8-movie'					=> ['negative'],
	'icons8-surface'				=> ['negativesize'],
	'icons8-transaction-list'		=> ['order'],
	'icons8-sheets'					=> ['paperstock'],
	'icons8-user'					=> ['person'],
	'icons8-xlarge-icons'			=> ['print'],
	'icons8-lab-items'				=> ['process'],
	'icons8-screwdriver'			=> ['repair'],
	'icons8-jpg'					=> ['scan'],
	'icons8-diversity'				=> ['series'],
	'icons8-exposure'				=> ['shutterspeed'],
	'icons8-small-lens'				=> ['teleconverter'],
	'icons8-test-tube'				=> ['toner'],
	'icons8-home'					=> ['home'],
	'icons8-facebook'				=> ['facebook'],
	'icons8-github'					=> ['github'],
	'icons8'						=> ['icons8'],
	'icons8-about'					=> ['about'],
	'icons8-login'					=> ['login'],
	'icons8-add-user-male'			=> ['register'],
	'icons8-sign-in-form-password'	=> ['password'],
	'icons8-bar-chart'				=> ['stats'],
	'icons8-help'					=> ['help'],
	'icons8-edit'					=> ['edit'],
	'icons8-add'					=> ['add'],
	'icons8-cancel'					=> ['no'],
	'icons8-ok'						=> ['yes'],
#unknown
#logout
);

# Define output directory
my $output = '../schema/static/svg';

# Get list of SVGs
my @files = `find svg -name '*.svg'`;

# Delete and recreate the dir
`rm -rf $output`;
`mkdir $output`;

foreach my $file (@files) {
	chomp $file;

	# Parse filename
	$file =~ m/^svg\/(.+)-\d+\.svg$/;
		
	# If a mapping exists	
	if ($newnames{$1}) {
		foreach my $newname (@{$newnames{$1}}) {
			# Copy SVG under new name
			copy($file, "$output/$newname.svg");
		}
	}
}
